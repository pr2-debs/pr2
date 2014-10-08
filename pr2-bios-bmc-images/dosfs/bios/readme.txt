================================================================================
QUANTA Computer Inc. BIOS RELEASE NOTES for S2A
================================================================================
Project Name	: S2A
BIOS Version	: S2A_3A03
Build Date	: 2009/02/11
Update BootBlock: YES
Clear CMOS	: YES
Clear NVRAM	: NO
Checksum	: 355C5BD6

================================================================================
                        HARDWARE REQUIREMENTS/REVISIONS
================================================================================
System hardware revision supported: S2A DVT2 (rev. C2B) and PVT boards.

================================================================================
                        INTEL PROCESSOR MICORCODE REVISIONS
================================================================================

SRV_C_79 (2009/2/6)
----------------------+------------------------------------+-----------------
Filename              | Description                        | Stepping(s)     
----------------------+------------------------------------+-----------------
M03106A5_0000000D.TXT | Assembly format, Revision 0000000D | D-0 (Nehalem-EP)

SRV_B_80 (2008/12/03)
----------------------+------------------------------------+-----------------
Filename              | Description                        | Stepping(s)     
----------------------+------------------------------------+-----------------
M01106A4_0000000D.TXT | Assembly format, Revision 0000000D | C-0 (Nehalem-EP)
M01106A4_0000000D.TXT | Assembly format, Revision 0000000D | C-1 (Nehalem-EP)

SRV_D_32 (2008/10/06)
----------------------+------------------------------------+-----------------
Filename              | Description                        | Stepping(s)     
----------------------+------------------------------------+-----------------
M03106A0_FFFF001A.TXT | Assembly format, Revision FFFF001A | A-0 (Nehalem-EP)
M03106A1_FFFF000B.TXT | Assembly format, Revision FFFF000B | A-1 (Nehalem-EP)
M03106A2_FFFF0019.TXT | Assembly format, Revision FFFF0019 | B-0 (Nehalem-EP)

================================================================================
                        SYSTEM FIRMWARE REQUIREMENTS/REVISIONS
================================================================================
BMC (embedded in AST2050)	: 1.01
FRU and SDR Package		: N/A
VGA (embedded in AST2050) 	: 0.88.4c (2009/1/19)
Intel(R) ICH10R SATA RAID	: Production Version 8.6.0.1007 (2008/9/21)
Intel(R) 82575EB (ZOAR)		: 1.3.28
Intel(R) SPS F/W (ME)		: SPS_01.01.00.004
Intel(R) Thurley Reference Code	: 1.03 (Jan. 29, 2009)
  - CPU RC Version		: 1.01
  - QPI RC Version		: 1.00
  - Memory RC Version		: 1.03

================================================================================
                        IMPORTANT INSTALLATION NOTES
================================================================================
WARNING:  It is very important to follow the flash option provided in the batch
file (S2A.BAT) to update BIOS. Uisng incorrect flash option to flash BIOS may
cause damage to your system.

!!!!! Once update BIOS to ME F/W (2B01 ~ 3AXX) version, downgrade BIOS to  !!!!!
!!!!! without ME F/W revision (1A01 ~ 2A07) is inhibited.                  !!!!!

BIOS update utility (AFUDOS): v4.27
(1) Copy AFUDOS.EXE, BIOS ROM and batch file to a HD or USB Flash Drive, execute
    S2A.BAT under DOS environment and update finishes automatically.
(2) Reboot system and new BIOS runs.

Note: AFUDOS will not update ME F/W.

===============================================================================
                        BIOS RECOVERY INSTRUCTIONS
===============================================================================
WARNING: Don't recovery BIOS from with ME F/W (2B01 ~ 3AXX) to without
         ME F/W revision (1A01 ~ 2A07), and vice versa.

- Recovery process can be initiated by setting the recovery jumper (J1D1).
- Recovery process will not flash boot block and NVRAM.
- BIOS recovery can be accomplished from SATA CD and USB Mass Storage device. 
- The recovery media must contain the image file 'AMIBOOT.ROM' under the root
  directory. 
- The following steps illustrate the recovery process:
  (1) Turn off system and insert recovery media.
  (2) Set the recovery jumper from J1D1: 1-2 to 2-3.
  (3) Restore the recovery jumper to normal position (J1D1: 1-2).
  (4) Turn on system and BIOS will start recovery process.
  (5) The BIOS POST screen will appear and display the progress if the boot
      block video is supported.
  (6) Once the recovery is completed, 4 beeps would be heard to indicate
      recovery process successful and system will reboot with new BIOS.

Note:
(a) The jumper should be restored to normal position (J1D1: 1-2) before turn on
    system on step (4). Otherwise, recovery process may be invoked again after
    reboot.

================================================================================
                            KNOWN ISSUES/WORKAROUNDS
================================================================================
- Even though implement workaround for IOH sighting #3319506, 'C4 - Master abort
  address error' still occurred on each POST and then 'C4' is disabled.
- Since only one demand or patrol scrub can be in process at a time (refer to
  361864_Nehalem_EP_EDS_rev_1_5.pdf page 150: Section 3.12 Single Device Data
  Correction (SDDC) Support), default setting is using demand scrub.
- [QPI L0s and L1] needs to enable to support package C-state but it is not
  recommanded to enable it on Tylersburg-EP B2 or earily stepping.
- Onbaord 82575EB may assert 'Correctable error: Bad TLP Status (BIT6)' and
  BIT12 - 'Replay Timer Time-out' sometimes while install Windows 2008.
  Therefore, these two events had been disabled for onbaord 82575EB.
- S2A_3A03 upgrades to AMI new CPU module for Nehalem-EP, CMOS map is changed.
  Don't use S2A_3A01 and S2A_3A02 for S2A production.

================================================================================
                                FEATURES ADDED/MODIFY
================================================================================
S2A_3A03:
- Reserved enough memory for local and IO APIC.
- Update AMI EIP17341: to fix the power field in P state is not correct.
- Ignore Bus Master activity as gate to entering any C-state for Nehalem CPU.
- Update D-0 stepping processor signature 000106A5 (Nehalem-EP) to
  M03106A5_0000000D from M03106A5_00000004.
- Clear HECI2 interrupt status before enable HECI2 interrupt.
- Update Intel(R) Boot agent to Beta v13.2.8 from PV v13.2.7.
- Change CPU module to 8.00.15_CPU-i7_01.02 from 8.00.12_CPU-P4_3F.13.
- Update "Intel - NB: Tylersburg" to 8.00.15_NB-TYLERSBURG_13
  from 8.00.15_NB-TYLERSBURG_12.
- Update "PCI_EXPRESS - NB: Tylersburg" to 8.00.15_PCIE-1500-NB-TLSB_08
  from 8.00.15_PCIE-1500-NB-TLSB_07.
- Update "ACPI: North Bridge - Tylersburg" to 8.00.15_ACPI-3.0-NB-TLSB_08
  from 8.00.15_ACPI-3.0-NB-TLSB_07 to reserve memory for IOH APIC and RCBA.
- Enable support for Coarse-Grained Clock Gating.
- Update AMI "ACPI: Central Bridge - Nehalem" to fix incorrect APIC ID
  in the SRAT table.
- Update "Intel - CB: Nehalem" to 8.00.15_CB-NEHALEM_14 from
  8.00.15_CB-NEHALEM_13.
- Update "Thurley RC" to v1.03 (8.00.15_RC-NEHALEM_103) from
  v1.00 (8.00.15_RC-NEHALEM_100).
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_020 from 8.00.15_SB-ICH10_018.
- Modify 2 bits in the flash descriptor ICHSTR0 2:1 = 01b to force ICH to 
  detect IOH ESI on every training sequence.
- Change SPI flash UVSCC to 0x2011 from 0x2019.
- Update ME F/W to SPS_01.01.00.004 from SPS_01.00.03.024.
- Bug fixed BIOS doesn't display 'Unknown DIMM number' if incorrect DIMM
  number is logged into SEL.
- Bug fixed incorrect programming for ICH10R SATA controller.

S2A_3A02:
- Mask correctable error BIT6 - 'Bad TLP' and BIT12 - 'Replay Timer Time-out'
  while ZOAR (82575EB) is populated.
- Implement SMBIOS type 4 - Processor Family to Intel(R) Xeon (TM) (B3h) for
  Nehalem-EP.
- Set 'Targeted Content Distribution' in SMBIOS type 0.
- Implement AMI Template WHEA eModule (8.00.14_WHEA_00.02-Beta0).
- Display "Trusted Computing" to BIOS setup menu if TPM device is detected.
- Reserved memory used by HECI2 and I/O used by BMC.
- Update AST2050 VBIOS to 0.88.4c from 0.87.0c.
- Verify FRU common header before read other FRU area.

S2A_3A01:
- Update 82575EB (ZOAR) option ROM to v1.3.27 from v1.3.24.
- Updated copyright string to 2009 from 2008.

S2A_2B03:
- Implement debug setup option for SI engineer to enable/disable
  options.force_unused_links_into_L1.
- Implement debug setup option for EMI engineer to enable/disable spread
  spectrum.
- Restore Intel(R) Boot agent to PV v13.2.4 from Beta v13.2.8.
- Increase KCS IBF and OBF delay time to 10 seconds from 5 seconds.
- Move code segment for OEMBOARD to POST2_CSEG from POST_CSEG.
- Bug fixed incorrect DIMM SPD Frequency in SMBIOS type 17 and BMC WEBUI.
- Implement 'Unknown Sensor Number 0xYZ: ' before HEX string.
- Update "4M: SPI 64K BOOTBLOCK FLASH" to 8.00.14_FLASH-4MSPI64K_10
  from 8.00.14_FLASH-4MSPI64K_09.
- Update "ACPI 3.0" to 8.00.13_ACPI-3.0_10 from 8.00.13_ACPI-3.0_10_RC2.
- Implement workaround for IOH sighting #3319974, 3319936, 3319937.
- Update workaround for IOH sighting #3319635.
- Update Thurley RC to v1.00 from v0.94.
- LV DDR3 1.35V support.
- Modify MRC for DDR3_CPU1/2_P1V35_EN_N to be high for 1.5V
  and low for 1.35V.
- Update microcode for C-0/C-1 stepping processor signature 000106A4
  (Nehalem-EP) to M01106A4_0000000D from M01106A4_0000000C.
- Update microcode for D-0 stepping processor signature 000106A5 (Nehalem-EP)
  to M03106A5_00000004 from M03106A5_00000002.
        
S2A_2B02:
- Change ME Power Mode to 'ME Powered In S0 Only' from 'ME Powered In All Sx
  States'.
- Update ME F/W to SPS_01.00.05.002.0_Production from SPS_01.00.03.024.0_Gold.
- Add ME Support to setup menu (Advanced -> PCI Configuration).
- Update "Intel - CB: Nehalem" to 8.00.15_CB-NEHALEM_13 from
  8.00.15_CB-NEHALEM_12.
- Update "Nehalem RC" to 0.94 from 0.93.
- Prevent system from performing full reset to change the QPI frequency.
- Implement workaround (disable L0s for all QPI link) for IOH sighting #3319942:
  QPI CRC errors experienced during L0s entry could cause system hangs.
- Update "Intel - NB: Tylersburg" to 8.00.15_NB-TYLERSBURG_12
  from 8.00.15_NB-TYLERSBURG_11.
- Update "ACPI: North Bridge - Tylersburg" to 8.00.15_ACPI-3.0-NB-TLSB_07
  from 8.00.15_ACPI-3.0-NB-TLSB_06.
- Update "PCI_EXPRESS - NB: Tylersburg" to 8.00.15_PCIE-1500-NB-TLSB_07
  from 8.00.15_PCIE-1500-NB-TLSB_06.
- Implement workarond (disable L0s for IOH PCIE 1 and 5) for IOH sighting
  #3319926: Link degrades and surprise link downs (SLD) on PCIe.
- Since '#3319811: EOI to the I/OxAPIC can be blocked' is already fixed in B3
  Stepping, enable IOH IOxAPIC.
- Add a selection 'Enter Setup' at the end of Popup Menu list.
- Update "SMI - SB: ICH9" to 8.00.09_SMI-3.12.07-ICH9_014 from
  8.00.09_SMI-3.12.06-ICH9_013.
- Implement workaround for 'IOH sighting #3319866: QPI D2 error L1 exit'
  to change the severity of a D2 error to correctable from fatal.
- Don't Implement workaround for IOH sighting #3319689 on single IOH platform.
- Implement workaround for IOH sighting #3319776 (disbale B2),
  #3319902 (disable D1) and 3319938 (disable D0) if stepping is <= B3.
- Update Intel(R) Boot agent to Beta v13.2.8 from PV v13.2.4.
- Follow S2A_SISTAI_Tap_Value_2008_12_09.xls to update new QPI tap setting.
- Added detail description for System Event (Sensor Type 12h) SEL.
- Prevent PEF always disabled by BIOS.

S2A_2B01:
- Update CPU module to 8.00.12_CPU-P4_3F.13 from 8.00.12_CPU-P4_3F.12.
- Update "SMI - Thurley" (EIP16791) to 8.00.09_SMI-3.12.07 from
  8.00.09_SMI-3.12.06.
- Update "INTEL PPM DT" from AMI to support T State.
- Update "4M: SPI 64K BOOTBLOCK FLASH" to 8.00.14_FLASH-4MSPI64K_09
  from 8.00.14_FLASH-4MSPI64K_08.
- Update "4M: SPI 64k Bootblock" to 8.00.13_SPI-Intel-ICH8_1.11 from
  8.00.13_SPI-Intel-ICH8_1.09.
- Implement AMI TAG: EIP16791, EIP16791.1 and EIP16791.2 to support SMI for
  over 64 CPUs.
- Implement separated option to enable/disable C3/C6/C7. Therefore, User can
  disable processor C3 if Legacy Linux OS issues prevent exposing it.
- Enable ME subsystem support.

S2A_2A06:
- Prevent BIOS from setting invalid IP (0.0.0.0) to BMC.
- Update Intel(R) Thurley RC code to v0.93 from v0.92.
  (a) Update 'QPI RC' to 0.95RC1 from 0.90RC5.
  (b) Update 'Nehalem MRC' to 0.95RC1 from 0.91RC3.
- Updated copyright string to 2008.
- Avoid the NMI generated in SMI Flash progress.
- Since Serial port 2 is not only for SOL but also could be used via internal
  serial port connector, enable flow control to be selectable for serial port 2.
- Implement 3 beeps while there is no any memory detected.
- Implement 'POST Timeout' option to wait for user to press hotkey key (the
  default option is the same as previous setting to wait 5 seconds).
- Update "Nehalem RC" to 8.00.15_RC-NEHALEM_092 from 8.00.15_CB-NEHALEM_11.
- Update "Intel - CB: Nehalem" to 8.00.15_CB-NEHALEM_12 from
  8.00.15_CB-NEHALEM_11.
- Update ICH10R SATA RAID option to Production Version 8.6.0.1007
  from Production Candidate 8.5.0.1030.
- Update C-0/C-1 stepping processor signature 000106A4 (Nehalem-EP) to
  M01106A4_0000000C from M01106A4_0000000B.
- Update D-0 stepping processor signature 000106A5 (Nehalem-EP) to
  M03106A5_00000002 from M03106A5_FFFF0005.
- Added setup engine v0.61 source code.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_018 from 8.00.15_SB-ICH10_017.

S2A_2A05:
- Update SMBIOS type 11 from FRU 'Custom product info 1/2/3'.
- Using FRU: 'Board Area Info' - 'Manufacturer Name' for SMBIOS
  type 2 'Manufacturer'.
- Enabling FERR# Multiplexing (MSR 1F1h BIT0) for Nehalem-EP processor.
- Follow ICH10 BWG 2.3.1 to read registers to provide a coherency-enforcing
  event that ensures the write to a memeory-mapped register is complete.
- Implement PCIE error bit information event log for debug purpose.
  Default setting is disabled via [Advanced] -> [Preproduction Debug] ->
  [PCI Error Bit Logging]
- Invoke int-19 automatically while failed to boot.
- Get UUID from 'Get Device Guid' instead of specific FRU offset.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_017 from 8.00.15_SB-ICH10_015.
- Update "SMI - SB: ICH9" to 8.00.09_SMI-3.12.06-ICH9_013 from
  8.00.09_SMI-3.12.06-ICH9_011.
- Update "ACPI: South Bridge - ICH9" to 8.00.12_ACPI30_10_RC2-ICH9_021
  from 8.00.12_ACPI30_10_B1-ICH9_017.
- Update "PCI_EXPRESS - SB: ICH9" to 8.00.13_PCIE_03-sbICH9_011
  from 8.00.13_PCIE_00-sbICH9_010.

S2A_2A04:
- Using IOH Global Error Bit Number (0 ~ 31) for all IOH SEL EventData3.
- Update 368264_Tylersburg_IOH_36D_24D_SR_1.48.pdf Document Changes #11
  - 3319850: PCIE_LER_SS_CTRLSTS Register Description Change.
  (XPUNCERRSTS_Received PCIe Completion With URStatus Mask had been changed
  to BIT7 from BIT6).
- Update "4M: SPI 64K BOOTBLOCK FLASH" to 8.00.14_FLASH-4MSPI64K_08
  from 8.00.14_FLASH-4MSPI64K_07.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_015 from 8.00.15_SB-ICH10_013.
- Update "Nehalem RC" to 8.00.15_RC-NEHALEM_092 from 8.00.15_CB-NEHALEM_11.
- Update 'Nehalem MRC' to v0.91RC3 from v0.91RC2.
- Update "Intel - NB: Tylersburg" to 8.00.15_NB-TYLERSBURG_11
  from 8.00.15_NB-TYLERSBURG_10.
- Update "PCI_EXPRESS - NB: Tylersburg" to 8.00.15_PCIE-1500-NB-TLSB_06
  from 8.00.15_PCIE-1500-NB-TLSB_05.
- Update "ACPI: Central Bridge - Nehalem" to 8.00.15_ACPI-3.0-CB-NEHALEM_04
  from 8.00.15_ACPI-3.0-CB-NEHALEM_03. (Already done in S2A_r082_r01)
- Update "ACPI: North Bridge - Tylersburg" to 8.00.15_ACPI-3.0-NB-TLSB_06
  from 8.00.15_ACPI-3.0-NB-TLSB_05. 
- Update "ACPI: South Bridge - ICH9" to 8.00.12_ACPI30_10_B1-ICH9_017 from
  8.00.12_ACPI30_10_B1-ICH9_016.
- Update CPU module to 8.00.12_CPU-P4_3F.12 from 8.00.12_CPU-P4_3F.11.
- Based on PCIe Link Width Strapping to program 'maximum link width'
  and 'hide/show PCI-E root port'.
- Added microcode (M03106A5_FFFF0005) for Nehalem-EP D-0 stepping processor.
- Update "Intel VTd : CSP - Tylersburg" to 8.00.15_VTd-2.00.00-TB_003
  from 8.00.15_VTd-2.00.00-TB_002.
- Increase maximum HDD number to 16 from 12.
- Update AST2050 VBIOS to V08701 from V08609.

S2A_2A03:
- Implement APIC IRQ routing for Tylersburg-EP Crystal Beach 3.
- Prevent PCIE error per port exceeds maximum allowed error counts (10 times).
- Add [Active State Power-Management] to [PCI Configuration].
- Implement memory sparing feature and eventlog.
- Implement IOH errata #44 - 3319795: Running forced recovery with
  L0s results in a Surprise Link Down.
- Implement workaround for IOH errata #43 - 3319776, 3319689, 3319636: Various
  QPI error statuses are observed.
- Added Nehalem-EP memory options to [Memory Configuration].
- Added QPI options to [PCI Configuration].
- Update C-0/C-1 stepping processor signature 000106A4 (Nehalem-EP) to
  M01106A4_0000000B from M01106A4_00000007.
- Add 82576EB (Kawela) option ROM.
- Rearrange [PCI Configuration menu] to 'ONBOARD DEVICE' ->
  'ONBAORD NIC MAC ADDRESS' -> 'MISC CHIPSET FEATURE'.
- Always apply IOH errata #29 "3319419/3319687: Interop issue of some
  PCIe Gen1 cards with Gen2" for PCIe port 1 which connects to ZOAR
- Change default setting for [Demand Scrubbing] to [Enabled] from [Disabled].
- Update Thurley Reference Code to 0.91RC2 from 0.81.
- Update "Intel - CB: Nehalem" to 8.00.15_CB-NEHALEM_11 from 8.00.15_CB-NEHALEM_08.
- Update "ACPI: North Bridge - Tylersburg" to 8.00.15_ACPI-3.0-NB-TLSB_05
  from 8.00.15_ACPI-3.0-NB-TLSB_04.
- Update "PCI_EXPRESS - SB: ICH9" to 8.00.13_PCIE_00-sbICH9_010 from
  8.00.13_PCIE_00-sbICH9_009.
- Implement default setting for Digitally Controlled Potentiometer (ISL9072x).
- Update "SMI - SB: ICH9" to 8.00.09_SMI-3.12.06-ICH9_011 from
  8.00.09_SMI-3.12.03B6-ICH9_010.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_012 from 8.00.15_SB-ICH10_011.
- Update SREDIR to 8.00.03_SREDIR_03.01_BETA_8 from 8.00.03_SREDIR_03.01_BETA_7.
- Prevent waiting BMC ready two time (Bootblock and Post) while
  BMCFlash_SUPPORT is enabled.
- Update "4M: SPI 64K BOOTBLOCK FLASH" to 8.00.14_FLASH-4MSPI64K_07
  from 8.00.14_FLASH-4MSPI64K_06.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_013 from 8.00.15_SB-ICH10_012.

S2A_2A02:
- Implement DRHD, RMRR and ATSR to support Intel VT-d. It could be enabled and
  disabled via BIOS setup option [Advanced]->[PCI Confgiuration]->[Intel VT-d].
  Default setting is [Disabled].
- Implement IOH BSU v0.83 Documentation Changes item 1 - #10 and #11.
- Implement QPI tap setting.
- Update AMI Tag: CORE0064.1 to fix memory base 4KB alignment issue.
- Update AMI tag: EIP12141 to fix Hard Disk was show 100.0GB information when
  used 1TB HDD.
- Update C-0/C-1 stepping processor signature 000106A4 (Nehalem-EP) to
  M01106A4_00000007 from M03106A4_00000004.
- Implement Nehalem-EP C-State C3, C6 and C7. It could be enabled/disabled via
  BIOS setup option [Advanced]->[CPU Configuration]->[Intel(R) C-STATE tech].
  Default setting is [Enabled].
- Change FACP.Preferred_PM_Profile to "Enterprise Server" from "Desktop".
- Implement workaround for IOH sighting #3319776: QPI PhyResets causing
  QPI Errors to be flagged (Mask B6 - BIT5 and DG - BIT7).

S2A_2A01:
- Update "INTEL PPM DT" to 8.00.14_IPPMDT_01.03-Beta2 from
  8.00.14_IPPMDT_01.03-Beta1.
- Update "SMBIOS - Template" to 8.00.08_SMB-3.1.02_CORE_RC26 from
  8.00.08_SMB-3.1.02_CORE_RC25.
- Update "Intel - NB: Tylersburg" to 8.00.15_NB-TYLERSBURG_10
  from 8.00.15_NB-TYLERSBURG_08.
- Update "PCI_EXPRESS - NB: Tylersburg" to 8.00.15_PCIE-1500-NB-TLSB_05
  from 8.00.15_PCIE-1500-NB-TLSB_04.
- Update "SMI" to 8.00.09_SMI-3.12.06 from 8.00.09_SMI-3.12.05.
- Update "SMI - SB: ICH9" to 8.00.09_SMI-3.12.03B6-ICH9_010 from
  8.00.09_SMI-3.12.03B6-ICH9_009.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_011 from 8.00.15_SB-ICH10_009.
- Implement seperated SDR per DIMM socket.
- Decrease SMBIOS size to 1000h from 1400h.
- Update AMIUCP.EXE to v1.04 from v1.02 and AFUDOS.EXE to v4.26 from v4.24.

S2A_1A08:
- Update TCPA module to 8.00.15_TCPA_0.19 from 8.00.15_TCPA_0.14.Beta1.
- Update "SMI" to 8.00.09_SMI-3.12.05 from 8.00.09_SMI-3.12.04_Beta1.
- Update CPU module to 8.00.12_CPU-P4_3F.11 from 8.00.12_CPU-P4_3F.10.
- Update "Intel - SB: ICH10" to 8.00.15_SB-ICH10_009 from 8.00.15_SB-ICH10_008.
- Update 'PCI EXPRESS - Thurley' to 8.00.13_PCIE_03 from 8.00.15_PCIE_00.
- Update "MPS Table" to 8.00.13.MPSTable_12 from 8.00.13.MPSTable_11.
- Update "ACPI" to 8.00.13_ACPI-3.0_10_RC2 from 8.00.12_ACPI-3.0_10_beta1.
- Update "ACPI: Central Bridge - Nehalem" to 8.00.15_ACPI-3.0-CB-NEHALEM_03
  from 8.00.15_ACPI-3.0-CB-NEHALEM_03.
- Update "ACPI: North Bridge - Tylersburg" to 8.00.15_ACPI-3.0-NB-TLSB_04 from
  8.00.15_ACPI-3.0-NB-TLSB_03.
- Update "ACPI: South Bridge - ICH9" to 8.00.12_ACPI30_10_B1-ICH9_016 from
  8.00.12_ACPI30_10_B1-ICH9_015.
- Set max single-bit ECC error count (=10) to prevent system from sticking if 
  error asserts continuesly.
- Implement setup option to switch shared and dedicated NIC.
- Update C-0 stepping processor signature 000106A4 (Nehalem-EP) to
  M03106A4_00000004 from M03106A4_00000001.
- Implement IOH BSU v0.82 Documentation Changes 1: (6).

S2A_1A07:
- Update CPU module to 8.00.12_CPU-P4_3F.10 from 8.00.12_CPU-P4_3F.0F.
- Update Thurley Reference Code to v0.81 from v0.80.
- Update 82575EB (ZOAR) option ROM to v1.3.24 from v1.3.10.
- Update "ACPI: North Bridge - Tylersburg" to 8.00.15_ACPI-3.0-NB-TLSB_03
  from 8.00.15_ACPI-3.0-NB-TLSB_01.
- Update "Intel - NB: Tylersburg" to 8.00.15_NB-TYLERSBURG_08
  from 8.00.15_NB-TYLERSBURG_07.
- Update "PCI_EXPRESS - NB: Tylersburg" to 8.00.15_PCIE-1500-NB-TLSB_04
  from 8.00.15_PCIE-1500-NB-TLSB_03.
- Update "Display Logo (all formats)" to 8.00.08_DISPLAYLOGO_25 from
  8.00.08_DISPLAYLOGO_24.
- Update C-0 stepping processor signature 000106A4 (Nehalem-EP) to
  M03106A4_00000001 from M03106A4_FFFF000D.
- Find uncorrectable ECC error DIMM number for processor 2 (1-base).
- Implemented BIOS workaround for IOH sighting #3319157.
- Implemente Direct Cache Access (DCA) for Crystal Beach.
- Display POST error 5125h when no shadow space for option ROM.
- Log "Software NMI" while BIOS generates NMI.
- Implement Remote BIOS update via BMC. (Need BMC supports this feature.)

S2A_1A06:
- Implement BIOS workaround for IOH BSU v0.64.
  (1) 3319486: DEVCON2[3:0] not accurately set the completion timeout value.
  (2) 3319511: QPI Queue/Table overflow or underflow error is observed.
  (3) 3319635: Bandwidth very low for write traffic with noSnoop attribute set.
  (4) 3319546: Timeout values much larger than specified.
  (5) 3319506: Transactions to addresses above TOCM are not setting the Master
               Abort.
  (6) 3319530: In QPI L1 Power management mode, Link layer sends retryable flits
               after L1.Ack.
  (7) 3319126: PCIe RX L0s entry/exit issues.
  (8) 3319688: Some Gen2 endpoints will not complete the training in Gen2 mode.
  (9) 2309341: Extended Error Detect Mask Registers of all PCIe root ports mask
               error logging by default.
- Implement ECC eventlog for SBE and MBE.
- Implement IOH and PCIE event log.
- Update B-0 stepping processor signature 000106A2 (Nehalem-EP) to
  M03106A2_FFFF0019 from M03106A2_FFFF0013.
- Implement microcode M03106A4_FFFF000D for C-0 stepping processor signature
  000106A4 (Nehalem-EP).
- Configure SATA port 5 (0-base) to eSATA Setting to pass SATA GEN1/2 eye
  diagram.
- Set ACPI power state to BMC (S0, S1, S4, S5 and legacy off).
- Follow SI BIOS SetupMENU v061.xls to modify the related setup menu.
- Update USB2 to 8.00.04_USB-2.24.04_BETA2 from 8.00.04_USB-2.24.04_BETA.
- Update "SMI - SB: ICH9" to 8.00.09_SMI-3.12.03B6-ICH9_008 from
  8.00.09_SMI-3.12.03B6-ICH9_007.
- Update "INTEL PPM DT" to INTEL PPM DT to 8.00.14_IPPMDT_01.03-Beta1 from
  8.00.14_IPPMDT_01.03-Alpha0.
- Update CPU module to 8.00.12_CPU-P4_3F.0F from 8.00.12_CPU-P4_3F.0E_Beta2.
- Change "FSB Speed" to "BCLK Speed" for Nehalem-EP procesor.
- Load microcode to NBSP in addition before put it to sleep.

S2A_1A05:
- Implement setup option to enable/disable Crystal Beach / DMA.
- Change string of POST error code (0x0120 ~ 0x12F) to 'Thermal Failure detected
  by PROCHOT#.' from 'Thermal Trip Failure'.
- Allow BIOS to record 'POST Error (0012): CMOS Date/Time Not Set' and 'POST
  Error (0004): CMOS Setting Wrong' while CMOS loss.
- Add OEM NMI handler for POST and DOS to display 'H/W malfunction!' while NMI
  is asserted.
- Implement Local APIC NMI structure.
- Update IST to 8.00.14_IPPMDT_01.03-Alpha0 from 8.00.14_IPPMDT_01.02.
- Implement SMBIOS type 1, 2, 3, 8, 10h, 11h and 13h.
- Add some IO delay for AMI TAG: EIP12169 - save/restore CMOS index while BIOS
  trap INT09 vector. 
- Send CPU and DIMM information to BMC.
- Modify [PCI Configuration] to meet SI Spec.
- Update the ICH10R SATA RAID option to Production Candidate 8.5.0.1030 from
  Beta 8.5.0.1020.

S2A_1A04:
- Update 'CB: Nehalem' to 8.00.15_CB-NEHALEM_07 from 8.00.15_CB-NEHALEM_06.
- Update 'NB: Tylersburg' to 8.00.15_NB-TYLERSBURG_06 from
  8.00.15_NB-TYLERSBURG_05.
- Update 'PCI EXPRESS - Thurley' to 8.00.15_PCIE_00 from 8.00.13_BETA1_PCIE_02.
- Update '4GBPlus' to 8.00.01_4GBPLUS-1.00.08 from 8.00.01_4GBPLUS-1.00.07.
- Update 'CPU module' to 8.00.12_CPU-P4_3F.0E_Beta2 from
  8.00.12_CPU-P4_3F.0B_Alpha3.
- Update 'SREDIR' to 8.00.03_SREDIR_03.01_BETA_7 from
  8.00.03_SREDIR_03.01_BETA_6.
- Update 'SMBIOS' to 8.00.08_SMB-3.1.02_CORE_RC25 from
  8.00.08_SMB-3.1.02_CORE_RC24.
- Update "ACPI: South Bridge - ICH9" to 8.00.12_ACPI30_10_B1-ICH9_014 from
  8.00.12_ACPI30_10_B1-ICH9_012.
- Update "AHCI - ICH9" 8.00.14-AHCI10012-sbICH9_004 from
  8.00.14-AHCI10012-sbICH9_003.
- Update "PCI_EXPRESS - SB: ICH9" to 8.00.13_PCIE_00-sbICH9_008 from
  8.00.13_PCIE_00-sbICH9_007.
- Update "SMI - SB: ICH9" to 8.00.09_SMI-3.12.03B6-ICH9_007 from
  8.00.09_SMI-3.12.03B6-ICH9_003.
- Change 'eChipset - SB module' to ICH10 from ICH9.
- Implement IOAPIC for Tylersburg.
- Set the MAX P-STATE for all procesors during POST.
- Set default PCIE ScratchPad Registers for AMI Nehalem processor module.
- Implement A20M enabled/disabled feature.
- Since there is no OEM LOGO from customer, change default setting for
  [Quiet Boot] to [Disabled] from [Enabled].
- Report PCIE base address to E820 table.
- Since COMB is routing to BMC, force the flow control to [Hardware] and shade
  this option.
- Implement SMBIOS Type 9 for S2A.
- Implement SMBIOS type 10 for S2A.
- Implement SMBIOS type 11 - OEM STRINGS.
- Implement SMBIOS type 12 - SYSTEM CONFIGURATION OPTIONS.
- Follow new SI specification to implement [Disabled][Enabled with PXE]
  [Enable without PXE] for onboard NIC.
- Set transmitter setting to 110b for front panel USB (port 3 and 4).

S2A_1A03:
- Control AC power loss recovery (Power Off, Power On and Last State) by BIOS.
- Update the ICH10R SATA RAID option to ICH10 SATA RAID v8.5.0.1020 from ICH9R
  v7.6.0.1011
- Update Nehalem-EP B-0 stepping microcode to M03106A2_FFFF0013 from
  M03106A2_FFFF000E. 
- Display hotkey stirng (<F2>, <F11> and <F12>) on graphics logo.

S2A_1A02:
- Modify the ICH10R GPIO base address to 0x500.
- Update Nehalem-EP B-0 stepping microcode to M03106A2_FFFF000E from
  M03106A2_FFFF000D.
- Change the maximum time for waiting BMC ready to 120 from 60 seconds.
- Update module 'CB: Nehalem' to 8.00.15_CB-NEHALEM_07 from
  8.00.15_CB-NEHALEM_05.
- Update module 'NB: Tylersburg' to 8.00.15_NB-TYLERSBURG_06
  from 8.00.15_NB-TYLERSBURG_05.
- Update module 'Nehalem RC' to v0.80 from v0.76.
- Update Intel Thurley Platform Reference Code to v0.80 from v0.76.

S2A_1A01:
- Initial release for S2A POWER-ON board.

================================================================================
                                FEATURES REMOVED
================================================================================
S2A_3A03:
- N/A

S2A_3A02:
- N/A

S2A_3A01:
- Hide Preproduction debug menu.

S2A_2B03:
- N/A

S2A_2B02:
- N/A

S2A_2B01:
- N/A

S2A_2A06:
- Since BIOS support ESC sequence keys, remove AMI remote key (<F4> to enter
  setup menu and <F3> for POPUP MENU.) for console redirection.
- Remove hotkey <F2/F3> to change setup menu color.
- Remove POST string "EVALUATION COPY, NOT FOR SALE".

S2A_2A05:
- Remove BIOS recovery via USB dongle.
- Don't send UUID to BMC.
- Since ICH10R DMI interface only support L0s, remove L1 support from ICH10R DMI
  port.

S2A_2A04:
- N/A

S2A_2A03:
- Remove [Module Version] from [USB Configuration].
- Hide [A20M] from [CPU Configuration] Menu (default setting is [Enabled]).
- Hide [C State package limit setting], [C1 Auto Demotion] and [C3 Auto Demotion]
  from [CPU Configuration] Menu.

S2A_2A02:
- Bug fixed system hanging up at checkpoint 0x2A if onboard NICs are disbaled.

S2A_2A01:
- N/A

S2A_1A08:
- Follow IOH sighting #3319811 to avoid using the I/OxAPIC in the Tylersburg
  stepping B2 or lower, and use only the I/OxAPIC in the ICH component.

S2A_1A07:
- Remove workaround for BIOS ROM checksum failure while only populated 1 DIMM
  (1GB).

S2A_1A06:
- Follow SI BIOS SetupMENU v061.xls to hide unnecessary setup option.

S2A_1A05:
- N/A

S2A_1A04:
- Remove SMBIOS type 15 - SYSTEM EVENT LOG.

S2A_1A03:
- Remove AMI small logo.

S2A_1A02:
- Disable ICH10R onchip LAN 82567LM.

S2A_1A01:
- N/A.

================================================================================
                                ISSUES FIXED
================================================================================
S2A_3A03:
- N/A

S2A_3A02:
- Bug fixed incorrect Apic Id in the SRAT table while installing 1.86 GHz
  Nehalem-EP processor.
- Prevent system from hanging up at waiting for <F1> and <F2> while BMC is
  not responding.
- Bug fixed BIOS hanging up if BMC reports incorrect FRU Common Header offset
  (all 0xFF) to BIOS.
- Bug fixed sending processor and memory information to BMC two times.

S2A_3A01:
- Get main board FRU device ID from SDR before read main board FRU to fix 'BIOS
  cannot get main board FRU after update BMC v0.29'.

S2A_2B03:
- Bug fixed: QPI frequency cannot modify sometimes.

S2A_2B02:
- Bug fixed: incorrect porting for EHCIIR2.
- Bug fixed: incorrect applying workaround for IOH sighting #3319776,
  #3319636 and then D3, DG, B6 and B0 error log had been disabled on B3
  stepping.

S2A_2B01:
- Bug fixed: NMI doesn't assert for PCI-E fatal and uncorrectable error.
- Bug fixed: incorrect hiding/showing PCI-E root port via PEWIDTH[5:0].

S2A_2A06:
- Bug fixed incorrect L2 cache size while Nehalem-EP processor has only 2 Cores
  (for example: E5502 1.86 GHz).

S2A_2A05:
- Bug fixed: XPCORERRSTS[0] - 'PCI link bandwidth changed status' does not clear
  correctly while enable [Active State Power-Management].
- Bug fixed: incorrect programming for ICH10R chipset configuration register
  1A8h (ICH10 EDS Rev:2.1: 10.1.35 LCTL¡XLink Control Register).

S2A_2A04:
- Bug fixed system hanging up at MBE SMI while only one processor
  populated and MBE occurrs.
- Bug fixed incorrect switching shared and dedicated NIC.

S2A_2A03:
- Bug fixed incorrect Apic Id in SRAT table while Hyper-Threadingis disabled.
- Bug fixed IOH root port PCI-E error status doesn't clear.
- Bug fixed: serial ports are disabled but [Remote Access] or [Serial Port Number]
  are enabled.
- Bug fixed: #102768 - System event log records some error messages about 'acpi'
  after install W2k3SP2x86.
- Implement Workaround of SATA2 HDD info is abnormal during post screen after
  press power button on AHCI mode.
- Bug fixed: #124471 - Install Windows 2008 was fail sometimes.

S2A_2A02:
- N/A

S2A_2A01:
- Bug fixed: missing workaround for "BIOS ROM checksum failure while only
  populated 1 DIMM (1GB)".
- Bug fixed: incorrect BMC F/W revision displays during POST.
- Bug fixed: failing to wake system from S4 while GPRW() assign S5.
- Bug fixed: #104532 - Some devices display wrong SID/SVID under RU.

S2A_1A08:
- Bug fixed: incorrect IOH BSU v0.82 Documentation Changes 1: (4).

S2A_1A07:
- Bug fixed: incorrect workaround for IOH sighting #3319126/3319688.

S2A_1A06:
- Bug fixed: incorrect porting for ICH10R RCRB CIR10 (offset 352Ch) and DMIC
  (offset 0234h)

S2A_1A05:
- Bug fixed: #102418 - BIOS SETUP Utility detected incorrect CPU info.
- Bug fixed: #103077 - BIOS setup utility dose not display Cache L3 in "CPU
  Configuration" page.

S2A_1A04:
- Modify the [Event Logging] help string to prevent user from confusing.
- AMI TAG: EIP13662 - Bug fixed: IBM USB keyboard may not work when this device 
           connect behind the USB 2.0 HUB.
- AMI TAG: USB0148 - USB keyboard may not work on LEGACY FREE system when CPU is 
           Nehalem(INTEL CPU).
- AMI TAG: EIP12079 - System may hang up when install RHEL 4.0 UP4.
- AMI TAG: EIP12169 - save/restore CMOS index while BIOS trap INT09 vector.

S2A_1A03:
- Bug fixed: NB PCIE port 8 had been hidden.
- Bug fixed: jumper message is missing.
- Bug fixed: #102417 - Error message on screen when boot from SATA HDD(Non OS).
- Bug fixed: system hanging up at reading file while performing bootblock
  recovery.

S2A_1A02:
- Bug fixed: failing to shut down in Linux while XEN is enabled.
- Add option ROM to dummy non-critical block (1st block) to prevent system from
  hanging up at checkpoint 0x20 after AC-ON-OFF.
- Bug fixed: failing to disable LOM2.
- Bug fixed: BIOS ROM checksum failure while only 1 DIMM (1GB) populated.

S2A_1A01:
- N/A.

[END OF RELEASE NOTES]