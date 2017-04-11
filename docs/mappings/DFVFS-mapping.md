---
title: DFVFS CASE UCO mapping
---

# DFVFS CASE UCO mapping


## BDEPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|password|??|??|
|recovery_password|??|??|
|startup_key|??|??|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace


## CompressedPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|compression_method|uco-observable.CompressedStream (from parent)*|uco-observable.CompressedStream.compressionMethod|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decompressed-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*


## CPIOPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "CPIO"|
|location|uco-observable.File|uco-observable.File.filePath
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location


## DataRangePathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|range_offset|uco-core.Relationship|uco-observable.DataRange.rangeOffset|
|range_size|uco-core.Relationship|uco-observable.DataRange.rangeSize|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace


## EncodedPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|encoding_method|uco-observable.EncodedStream (from parent)*|uco-observable.EncodedStream.encodingMethod|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decoded-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*


## EncryptedPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|cipher_mode|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionMode|
|encryption_method|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionMethod|
|initialization_vector|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionIV|
|key|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionKey|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decrypted-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*


## EWFPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="EWF"|
|parent|-|*(no Relationship is created)*|


## FVDEPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|encrypted_root_plist|??|??|
|password|??|??|
|recovery_password|??|??|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace


## GzipPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.CompressedStream (from parent)*|uco-observable.CompressedStream.compressionMethod="GZIP"|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decompressed-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*


## LVMPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "LVM"|
|location|uco-observable.File|uco-observable.File.filePath|
|volume_index|uco-object.Volume|uco-observable.Volume.volumeID|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location


## NTFSPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "NTFS"|
|location|uco-observable.File|uco-observable.File.filePath|
|data_stream|uco-observable.AlternateDataStream|uco-observable.AlternateDataStream.name|
|mft_attribute|-|-|
|mft_entry|-|-|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location


## OSPathSpec
*This is the root PathSpec. It doesn't have a parent or file system property.
It is simply the original file path given to DFVFS.
Tools outside of DFVFS should create Relationships to this Trace providing context
to the physical device.*

|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|location|uco-observable.File|uco-observable.File.filePath|


## QCOWPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="QCOW"|
|parent|-|*(no Relationship is created)*|


## RAWPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="RAW"|
|parent|-|*(no Relationship is created)*|


## SQLiteBlobPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|column_name|uco-core.Relationship|uco-observable.SQLiteBlob.columnName|
|row_condition|uco-core.Relationship|uco-observable.SQLiteBlob.rowCondition|
|row_index|uco-core.Relationship|uco-observable.SQLiteBlob.rowIndex|
|table_name|uco-core.Relationship|uco-observable.SQLiteBlob.tableName|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace


## TARPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "TAR"|
|location|uco-observable.File|uco-observable.File.filePath|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location


## TSKPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|location|uco-observable.File|uco-observable.File.filePath|
|data_stream|??|??|
|inode|??|??|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location


## TSKPartitionPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Disk (from parent)*|uco-observable.Disk.partitionRefs = id of current trace (*TODO: Should we remove this property? Doesn't the Relationship suffice?*)|
|location OR part_index|uco-observable.DiskPartition|uco-observable.DiskPartition.partitionID|
|start_offset|uco-observable.DiskPartition|uco-observable.DiskPartition.partitionOffset|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace



## VHDIPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="VHDI"|
|parent|-|*(no Relationship is created)*|


## VMDKPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="VMDK"|
|parent|-|*(no Relationship is created)*|


## VShadowPathSpec
*TODO: Should we create a new property bundle for this?*

|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.DiskPartition|uco-observable.DiskPartition.diskPartitionType = "VSHADOW"|
|location OR store_index|uco-observable.DiskPartition|uco-observable.DiskPartition.partitionID|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace


## ZIPPathSpec
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "ZIP"|
|location|uco-observable.File|uco-observable.File.filePath|
|parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location



<sub>\*: While a Trace is created for this PathSpec. Its information
has been and placed as a property bundle on the Trace created by the PathSpec's
parent and on the Relationship that connects our blank uco-observable.File to the PathSpec's paren't uco-observable.File.
For example, if we have `CompressedStreamPathSpec -parent-> OSPathSpec`, the CompressedStream property bundle
will be added to the Trace created by the OSPathSpec and a blank Trace will
be created for itself. The blank Trace represents the decompressed version of the OSPathSpec file.
If we have `CompressedStreamPathSpec -parent-> EncryptedStreamPathSpec -parent-> OSPathSpec`, a blank
Trace will be created for CompressedStreamPathSpec, the CompressedStream property bundle will be placed on
the blank Trace created by the EncryptedStreamPathSpec which in turn has the EncryptedStream
property bundle on the Trace created by the OSPathSpec. (OSPathSpec's File property bundle will
be on the same Trace as EncryptedStream.)
