#include <sys/io.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>

uint8_t read_nvram_part(uint16_t addr_port, uint16_t data_port, uint8_t addr)
{
  //usleep(1000);
  outb_p(addr & 0x7F, addr_port);
  return inb_p(data_port);
}

uint8_t read_nvram(uint8_t addr)
{
  if (addr & 0x80)
    return read_nvram_part(0x72, 0x73, addr);
  else
    return read_nvram_part(0x70, 0x71, addr);
}

void write_nvram_part(uint16_t addr_port, uint16_t data_port, uint8_t addr, uint8_t value)
{
  //usleep(1000);
  asm volatile("cli");
  uint8_t outaddr = (addr & 0x7F);// | (inb_p(addr_port) & 0x80);
  outb_p(outaddr, addr_port);
  outb_p(value, data_port);
  asm volatile("sti");
}

void write_nvram(uint8_t addr, uint8_t value)
{
  if (addr & 0x80)
   write_nvram_part(0x72, 0x73, addr, value);
  else
    write_nvram_part(0x70, 0x71, addr, value);
}

int do_read(char *file)
{
  uint8_t buff[256];
  int i;
  FILE *f;

  int max_retries = 20;

  for (i = 0; i < sizeof(buff); i++)
  {
    if (i < 14)
    {
      buff[i] = 0;
      continue;
    }
    
    buff[i] = read_nvram(i);
    
    if (buff[i] != read_nvram(i)) // Ignore errors in clock.
    {
      fprintf(stderr, "An error occurred while reading address %i. %i %i ", i, buff[i], read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
    fprintf(stderr, "%i\n", read_nvram(i));
      i--;
      if (!(max_retries--))
      {
        fprintf(stderr, "Too many errors. Giving up.\n");
        return -1;
      }
      else
        fprintf(stderr, "Retrying.\n");
    }
  }

  if (strcmp(file, "-"))
  {
    f = fopen(file, "w");
    if (!f)
    {
      perror("Error opening file");
      return 1;
    }
  }
  else
  {
    f = stdout;
  }

  if (fwrite(buff, sizeof(buff), 1, f) != 1)
  {
    perror("Writing data to file failed");
    fclose(f);
    return 1;
  }

  fprintf(stderr, "Success!\n");
  fclose(f);
  return 0;
}

int do_write(char *file)
{
  uint8_t buff[256];
  int i;
  FILE *f;
  int max_retries = 20;
  int had_error = 0;

  if (!(f = fopen(file, "r")))
  {
    perror("Error opening file");
    return 1;
  }

  if (!fread(buff, sizeof(buff), 1, f))
  {
    perror("Reading data failed");
    fclose(f);
    return 1;
  }

  fgetc(f);
  if (!feof(f))
  {
    fprintf(stderr, "File should be exactly 256 bytes long.\n");
    return 1;
  }

  fclose(f);
  
  while (1)
  {
    // Don't write the time, start at 14.
    for (i = 14; i < sizeof(buff); i++)
      write_nvram(i, buff[i]);
    
    had_error = 0;
    for (i = 14; i < sizeof(buff); i++)
      if (read_nvram(i) != buff[i])
      {
        fprintf(stderr, "Mismatch at address %i.\n", i);
        had_error = 1;
      }

    if (!had_error)
      break;
    
    if (!(max_retries--))
    {
      fprintf(stderr, "Too many errors. Aborting.\n");
      return 1;
    }

    fprintf(stderr, "An error occurred while writing. Will retry the whole write.\n");
  }

  if (had_error)
    fprintf(stderr, "Writing succeeded in the end, but the system time may have been clobbered.\n");
  
  return had_error;
}

int main(int argc, char **argv)
{
  if (ioperm(0x70, 4, 1) != 0)
  {
    perror("Are you root? Call to ioperm failed");
    return -1;
  }
  
  if (iopl(3) != 0)
  {
    perror("Are you root? Call to iopl failed");
    return -1;
  }

  if (argc != 3)
    {}
  else if (!strcmp(argv[1], "-r"))
  {
    return do_read(argv[2]);
  }
  else if (!strcmp(argv[1], "-w"))
  {
    return do_write(argv[2]);
  }

  printf("usage: user-nvram -r <destination_file>\n");
  printf("       user-nvram -w <source_file>\n");
  printf("\n");
  printf("Read (-r) or write (-r) a 256 byte nvram.\n");
  return 1;
}
