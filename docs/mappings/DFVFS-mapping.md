---
title: DFVFS CASE UCO mapping
---

# DFVFS CASE UCO mapping
Mappings for [Digital Forensics Virtual File System (DFVFS)](https://github.com/log2timeline/dfvfs).

*(TODO: The VFSStat.type can also define pipes, sockets, links, and devices. Where should we put this information?)*


### Legend
- `-` = Attribute is ignored and not mapped.
- `??` = There is a GAP in an available UCO property.


## BDE
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|BDEPathSpec.password|??|??|
|BDEPathSpec.recovery_password|??|??|
|BDEPathSpec.startup_key|??|??|
|BDEPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace


## CompressedStream
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|CompressedStreamPathSpec.compression_method|uco-observable.CompressedStream (from parent)*|uco-observable.CompressedStream.compressionMethod|
|CompressedStreamPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decompressed-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*


## CPIO
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "CPIO"|
|CPIOPathSpec.location|uco-observable.File|uco-observable.File.filePath
|CPIOPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location
|CPIOFileEntry.VFSStat.gid|??|??|
|CPIOFileEntry.VFSStat.uid|??|??|
|CPIOFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## DataRange
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|DataRangePathSpec.range_offset|uco-core.Relationship|uco-observable.DataRange.rangeOffset|
|DataRangePathSpec.range_size|uco-core.Relationship|uco-observable.DataRange.rangeSize|
|DataRangePathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace
|DataRangeFileEntry.VFSStat.size|uco-observable.ContentData|uco-observable.ContentData.sizeInBytes|


## EncodedStream
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|EncodedStreamPathSpec.encoding_method|uco-observable.EncodedStream (from parent)*|uco-observable.EncodedStream.encodingMethod|
|EncodedStreamPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decoded-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*
|EncodedStreamFileEntry.VFSStat.size|uco-observable.ContentData|uco-observable.ContentData.sizeInBytes|


## EncryptedStream
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|EncryptedStreamPathSpec.cipher_mode|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionMode|
|EncryptedStreamPathSpec.encryption_method|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionMethod|
|EncryptedStreamPathSpec.initialization_vector|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionIV|
|EncryptedStreamPathSpec.key|uco-observable.EncryptedStream (from parent)*|uco-observable.EncryptedStream.encryptionKey|
|EncryptedStreamPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decrypted-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*
|EncryptedStreamFileEntry.VFSStat.size|uco-observable.ContentData|uco-observable.ContentData.sizeInBytes|


## EWF
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="EWF"|
|EWFPathSpec.parent|-|*(no Relationship is created)*|


## FVDE
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|FVDEPathSpec.encrypted_root_plist|??|??|
|FVDEPathSpec.password|??|??|
|FVDEPathSpec.recovery_password|??|??|
|FVDEPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace
|FVDEFileEntry.VFSStat.size|??|??|


## Gzip
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.CompressedStream (from parent)*|uco-observable.CompressedStream.compressionMethod="GZIP"|
|GzipPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="decompressed-from"<br>uco-core.Relationship.source=id of current trace<br>uco-core.Relationship.target=id of parent trace<br>*(also contains property bundles defined in above rows)*
|GzipFileEntry.VFSStat.size|uco-observable.ContentData|uco-observable.ContentData.sizeInBytes|


## LVM
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "LVM"|
|LVMPathSpec.location|uco-observable.File|uco-observable.File.filePath|
|LVMPathSpec.volume_index|uco-object.Volume|uco-observable.Volume.volumeID|
|LVMPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location
|LVMFileEntry.VFSStat.size|uco-observable.File|uco_observable.File.sizeInBytes|
|LVMFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## NTFS
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "NTFS"|
|NTFSPathSpec.location|uco-observable.File|uco-observable.File.filePath|
|NTFSPathSpec.data_stream|uco-observable.AlternateDataStream|uco-observable.AlternateDataStream.name|
|NTFSPathSpec.mft_attribute|-|-|
|NTFSPathSpec.mft_entry|-|-|
|NTFSPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location
|NTFSFileEntry.attributes.FileNameNTFSAttribute.access_time|uco-observable.MftRecord|uco-observable.MftRecord.mftFileNameAccessedTime|
|NTFSFileEntry.attributes.FileNameNTFSAttribute.creation_time|uco-observable.MftRecord|uco-observable.MftRecord.mftFileNameCreatedTime|
|NTFSFileEntry.attributes.FileNameNTFSAttribute.entry_modification_time|uco-observable.MftRecord|uco-observable.MftRecord.mftFileNameRecordChangeTime|
|NTFSFileEntry.attributes.FileNameNTFSAttribute.modification_time|uco-observable.MftRecord|uco-observable.MftRecord.mftFileNameModifiedTime|
|NTFSFileEntry.attributes.FileNameNTFSAttribute.file_attribute_flags|uco-observable.MftRecord|uco-observable.MftRecord.mftFlags|
|NTFSFileEntry.attributes.FileNameNTFSAttribute.name|uco-observable.MftRecord|uco-observable.MftRecord.mftFileID *(TODO: Confirm this.)*|
|NTFSFileEntry.attributes.FileNameNTFSAttribute.parent_file_reference|uco-observable.MftRecord|uco-observable.MftRecord.mftParentID|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.access_time|??|??|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.creation_time|??|??|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.entry_modification_time|??|??|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.modification_time|??|??|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.file_attribute_flags|??|??|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.owner_identifier|uco-observable.MftRecord|uco-observable.MftRecord.ntfsOwnerID|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.security_descriptor_identifier|uco-observable.MftRecord|uco-observable.MftRecord.ntfsOwnerSID|
|NTFSFileEntry.attributes.StandardInformationNTFSAttribute.update_sequence_number|??|??|
|NTFSFileEntry.attributes.ObjectIdentifierNTFSAttribute.droid_file_identifier|??|??|
|NTFSFileEntry.attributes.SecurityDescriptorNTFSAttribute.security_descriptor|uco-observable.NTFSFileSystem|uco-observable.NTFSFileSystem.sid|
|NTFSFileEntry.VFSStat.size|uco-observable.File|uco_observable.File.sizeInBytes|
|NTFSFileEntry.VFSStat.atime|uco-observable.File|uco-observable.File.accessedTime|
|NTFSFileEntry.VFSStat.ctime|uco-observable.File|uco-observable.File.createdTime|
|NTFSFileEntry.VFSStat.crtime|uco-observable.File|uco-observable.File.metadataChangeTime|
|NTFSFileEntry.VFSStat.mtime|uco-observable.File|uco-observable.File.modifiedTime|
|NTFSFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## OS
*This is the root FileEntry/PathSpec. It doesn't have a parent or file system property.
It is simply the original file path given to DFVFS.
Tools outside of DFVFS should create Relationships to this Trace providing context
to the physical device.*

|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|OSPathSpec.location|uco-observable.File|uco-observable.File.filePath|
|OSFileEntry.VFSStat.size|uco-observable.File|uco_observable.File.sizeInBytes|
|OSFileEntry.VFSStat.atime|uco-observable.File|uco-observable.File.accessedTime|
|OSFileEntry.VFSStat.ctime|uco-observable.File|uco-observable.File.createdTime|
|OSFileEntry.VFSStat.mtime|uco-observable.File|uco-observable.File.modifiedTime|
|OSFileEntry.VFSStat.mode|??|??|
|OSFileEntry.VFSStat.uid|??|??|
|OSFileEntry.VFSStat.gid|??|??|
|OSFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## QCOW
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="QCOW"|
|QCOWPathSpec.parent|-|*(no Relationship is created)*|


## RAW
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="RAW"|
|RAWPathSpec.parent|-|*(no Relationship is created)*|


## SQLiteBlob
*NOTE: If SQLiteBlobFileEntry.VFSStat.type == FILE_ENTRY_TYPE_DIRECTORY it shouldn't be

|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|SQLiteBlobPathSpec.column_name|uco-core.Relationship|uco-observable.SQLiteBlob.columnName|
|SQLiteBlobPathSpec.row_condition|uco-core.Relationship|uco-observable.SQLiteBlob.rowCondition|
|SQLiteBlobPathSpec.row_index|uco-core.Relationship|uco-observable.SQLiteBlob.rowIndex|
|SQLiteBlobPathSpec.table_name|uco-core.Relationship|uco-observable.SQLiteBlob.tableName|
|SQLiteBlobPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace
|SQLiteBlobFileEntry.VFSStat.size|uco-observable.ContentData|uco-observable.ContentData.sizeInBytes|
|SQLiteBlobFileEntry.VFSStat.type|-|*(When type == FILE_ENTRY_TYPE_DIRECTORY this means that only the table_name and column_name has been specified. It is treated as a virtual directory in DFVFS, but we will ignore this for UCO.)*|



## TAR
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "TAR"|
|TARPathSpec.location|uco-observable.File|uco-observable.File.filePath|
|TARPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location
|TARFileEntry.VFSStat.size|uco-observable.File|uco_observable.File.sizeInBytes|
|TARFileEntry.VFSStat.mtime|uco-observable.File|uco-observable.File.modifiedTime|
|TARFileEntry.VFSStat.mode|??|??|
|TARFileEntry.VFSStat.uid|??|??|
|TARFileEntry.VFSStat.gid|??|??|
|TARFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## TSK
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|TSKPathSpec.location|uco-observable.File|uco-observable.File.filePath|
|TSKPathSpec.data_stream|??|??|
|TSKPathSpec.inode|??|??|
|TSKPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location
|TSKFileEntry.VFSStat.size|uco-observable.File|uco_observable.File.sizeInBytes|
|TSKFileEntry.VFSStat.atime|uco-observable.File|uco-observable.File.accessedTime|
|TSKFileEntry.VFSStat.bkup|??|??|
|TSKFileEntry.VFSStat.ctime|uco-observable.File|uco-observable.File.createdTime|
|TSKFileEntry.VFSStat.crtime|uco-observable.File|uco-observable.File.metadataChangeTime|
|TSKFileEntry.VFSStat.dtime|uco-observable.ExtInode|uco-observable.ExtInode.extDeletionTime|
|TSKFileEntry.VFSStat.mtime|uco-observable.File|uco-observable.File.modifiedTime|
|TSKFileEntry.VFSStat.mode|??|??|
|TSKFileEntry.VFSStat.uid|??|??|
|TSKFileEntry.VFSStat.gid|??|??|
|TSKFileEntry.VFSStat.ino|??|??|
|TSKFileEntry.VFSStat.is_allocated|??|??|
|TSKFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## TSKPartition
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Disk (from parent)*|uco-observable.Disk.partitionRefs = id of current trace (*TODO: Should we remove this property? Doesn't the Relationship suffice?*)|
|TSKPartitionPathSpec.location OR part_index|uco-observable.DiskPartition|uco-observable.DiskPartition.partitionID|
|TSKPartitionPathSpec.start_offset|uco-observable.DiskPartition|uco-observable.DiskPartition.partitionOffset|
|TSKPartitionPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace
|TSKPartitionFileEntry.VFSStat.size|uco-observable.ContentData|uco_observable.ContentData.sizeInBytes|
|TSKPartitionFileEntry.VFSStat.is_allocated|??|??|
|TSKPartitionFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|



## VHDI
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="VHDI"|
|VHDIPathSpec.parent|-|*(no Relationship is created)*|


## VMDK
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.Image (from parent)*|uco-observable.Image.imageType="VMDK"|
|VMDKPathSpec.parent|-|*(no Relationship is created)*|


## VShadow
*TODO: Should we create a new property bundle for this?*

|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.DiskPartition|uco-observable.DiskPartition.diskPartitionType = "VSHADOW"|
|VShadowPathSpec.location OR store_index|uco-observable.DiskPartition|uco-observable.DiskPartition.partitionID|
|VShadowPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace
|VShadowFileEntry.VFSStat.size|uco-observable.ContentData|uco_observable.ContentData.sizeInBytes|
|VShadowFileEntry.VFSStat.crtime|uco-observable.File|uco-observable.File.metadataChangeTime|
|VShadowFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


## ZIP
|DFVFS|CASE/UCO Class|CASE/UCO Property|
|---|---|---|
|-|uco-observable.File|uco-observable.File.fileSystemType = "ZIP"|
|ZIPPathSpec.location|uco-observable.File|uco-observable.File.filePath|
|ZIPPathSpec.parent|uco-core.Relationship|uco-core.Relationship.kindOfRelationship="contained-within"<br>uco-core.Relationship.source = id of current trace<br>uco-core.Relationship.target = id of parent trace<br>uco-core.Relationship.PathRelation.path = location
|ZIPFileEntry.VFSStat.size|uco-observable.File|uco_observable.File.sizeInBytes|
|ZIPFileEntry.VFSStat.mtime|uco-observable.File|uco-observable.File.modifiedTime|
|ZIPFileEntry.VFSStat.mode|??|??|
|ZIPFileEntry.VFSStat.type|uco-observable.File|uco-observable.File.isDirectory = (type == FILE_ENTRY_TYPE_DIRECTORY)|


<sub>\*: While a Trace is created for this PathSpec. Its information
has been and placed as a property bundle on the Trace created by the PathSpec's
parent and on the Relationship that connects our blank Trace to the PathSpec's parent Trace.
For example, if we have `CompressedStreamPathSpec -parent-> OSPathSpec`, the CompressedStream property bundle
will be added to the Trace created by the OSPathSpec and a blank Trace will
be created for itself. The blank Trace represents the decompressed version of the OSPathSpec file.
If we have `CompressedStreamPathSpec -parent-> EncryptedStreamPathSpec -parent-> OSPathSpec`, a blank
Trace will be created for CompressedStreamPathSpec, the CompressedStream property bundle will be placed on
the blank Trace created by the EncryptedStreamPathSpec which in turn has the EncryptedStream
property bundle on the Trace created by the OSPathSpec. (OSPathSpec's File property bundle will
be on the same Trace as EncryptedStream.)
