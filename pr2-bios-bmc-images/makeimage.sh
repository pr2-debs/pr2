#! /bin/sh
IMAGE_NAME=$1
AUTORUN_NAME=$2

if test "foo_$IMAGE_NAME" = "foo_"; then
  echo usage $0 destination-name default-batch-file
  exit 1
fi

echo Creating image "$IMAGE_NAME"...

gunzip -c freedos-base.img.gz > "$IMAGE_NAME"
sudo mount "$IMAGE_NAME" ./mount_point -o loop,offset=32256,rw
cp -r dosfs dosfs_tmp
find dosfs_tmp -name .\* -exec rm -rf \{\} \; 2> /dev/null
tar xzf fdos.tgz -C dosfs_tmp
sudo cp -r dosfs_tmp/* mount_point
rm -rf dosfs_tmp

if test "foo_$AUTORUN_NAME" != "foo_"; then
  echo Copying "$AUTORUN_NAME" into default.bat
  if test -e $AUTORUN_NAME; then
    sudo cp $AUTORUN_NAME mount_point/default.bat
  else
    echo File "$AUTORUN_NAME" does not exist.
  fi
fi

sudo umount ./mount_point

echo
echo Image should be ready. You can test it by running:
echo "  "  qemu -hda '"'$IMAGE_NAME'"'
echo You can mount it by typing:
echo "  "  sudo mount '"'$IMAGE_NAME'"' ./mount_point -o loop,offset=32256,rw
