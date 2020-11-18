# UCO 0.5.0 Release Notes

## Focus:

UCO Version 0.5.0 is primarily focused on the removal of the investigation namespace from UCO (that namespace now resides in the CASE ontology) and on the renaming of several classes (Observable subclasses, Facet subclasses) in the observable namespace  and a single property (core:facet) to support improved alignment with the CASE ontology and the forthcoming addition of ObservableObject subclasses.

### Focus Exceptions: 


# Changes (these are changes to ontologies, classes or properties in the preexisting ontology)

### Breaking Changes (these are changes to ontologies, classes or properties in the preexisting ontology that make the new release non-backward-compatible)

* uco-observable: modified the class name of observable:CyberItem to be observable:ObservableObject - [Issue OC-7](https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-7)
* uco-observable: modified the class name of observable:CyberAction to be observable:ObservableAction - [Issue OC-7](https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-7)
* uco-observable: modified the class name of observable:CyberRelationship to be observable:ObservableRelationship - [Issue OC-7](https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-7)
* uco-observable: modified the class name of observable:CyberObservablePattern to be observable:ObservablePattern - [Issue OC-7](https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-7)
* uco-core: modified the property name of core:facets to be core:hasFacet - [Issue OC-58](https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-58)
* uco-observable: renamed the Facet subclasses within the observable namespace by appending “Facet” to the end of each subclass name - [Issue OC-57](https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-57)

	Deprecated Subclass Name | New Subclass Name
	------------------------ | -----------------
	observable:Account | observable:AccountFacet
	observable:AccountAuthentication | observable:AccountAuthenticationFacet
	observable:Application | observable:ApplicationFacet
	observable:ApplicationAccount | observable:ApplicationAccountFacet
	observable:ArchiveFile | observable:ArchiveFileFacet
	observable:Attachment | observable:AttachmentFacet
	observable:Audio | observable:AudioFacet
	observable:AutonomousSystem | observable:AutonomousSystemFacet
	observable:BluetoothAddress | observable:BluetoothAddressFacet
	observable:BrowserBookmark | observable:BrowserBookmarkFacet
	observable:BrowserCookie | observable:BrowserCookieFacet
	observable:Calendar | observable:CalendarFacet
	observable:CalendarEntry | observable:CalendarEntryFacet
	observable:CompressedStream | observable:CompressedStreamFacet
	observable:ComputerSpecification | observable:ComputerSpecificationFacet
	observable:Contact | observable:ContactFacet
	observable:ContentData | observable:ContentDataFacet
	observable:DataRange | observable:DataRangeFacet
	observable:Device | observable:DeviceFacet
	observable:DigitalAccount | observable:DigitalAccountFacet
	observable:DigitalSignatureInfo | observable:DigitalSignatureInfoFacet
	observable:Disk | observable:DiskFacet
	observable:DiskPartition | observable:DiskPartitionFacet
	observable:DomainName | observable:DomainNameFacet
	observable:EXIF | observable:EXIFFacet 
	observable:EmailAccount | observable:EmailAccountFacet
	observable:EmailAddress |observable:EmailAddressFacet
	observable:EmailMessage |observable:EmailMessageFacet
	observable:EncodedStream |observable:EncodedStreamFacet
	observable:EncryptedStream |observable:EncryptedStreamFacet
	observable:Event |observable:EventFacet
	observable:ExtInode |observable:ExtInodeFacet
	observable:ExtractedStrings |observable:ExtractedStringsFacet
	observable:File |observable:FileFacet
	observable:FilePermissions |observable:FilePermissionsFacet
	observable:FileSystem |observable:FileSystemFacet
	observable:Fragment |observable:FragmentFacet
	observable:GeoLocationEntry |observable:GeoLocationEntryFacet
	observable:GeoLocationLog |observable:GeoLocationLogFacet
	observable:GeoLocationTrack |observable:GeoLocationTrackFacet
	observable:HTTPConnection |observable:HTTPConnectionFacet
	observable:ICMPConnection |observable:ICMPConnectionFacet
	observable:IPv4Address |observable:IPv4AddressFacet
	observable:IPv6Address |observable:IPv6AddressFacet
	observable:Image |observable:ImageFacet
	observable:Library |observable:LibraryFacet
	observable:MACAddress |observable:MACAddressFacet
	observable:Memory |observable:MemoryFacet
	observable:Message |observable:MessageFacet
	observable:MessageThread |observable:MessageThreadFacet
	observable:MftRecord |observable:MftRecordFacet
	observable:MobileAccount |observable:MobileAccountFacet
	observable:MobileDevice |observable:MobileDeviceFacet
	observable:Mutex |observable:MutexFacet
	observable:NTFSFilePermissions |observable:NTFSFilePermissionsFacet
	observable:NTFSFileSystem |observable:NTFSFileSystemFacet
	observable:NetworkConnection |observable:NetworkConnectionFacet
	observable:NetworkFlow |observable:NetworkFlowFacet
	observable:NetworkInterface |observable:NetworkInterfaceFacet
	observable:Note |observable:NoteFacet
	observable:OperatingSystem |observable:OperatingSystemFacet
	observable:PDFFile |observable:PDFFileFacet
	observable:PathRelation |observable:PathRelationFacet
	observable:PhoneAccount |observable:PhoneAccountFacet
	observable:PhoneCall |observable:PhoneCallFacet
	observable:Process |observable:ProcessFacet
	observable:PropertiesEnumeratedEffect |observable:PropertiesEnumeratedEffectFacet
	observable:PropertyReadEffect |observable:PropertyReadEffectFacet
	observable:RasterPicture |observable:RasterPictureFacet
	observable:SIMCard |observable:SIMCardFacet
	observable:SMSMessage |observable:SMSMessageFacet
	observable:SQLiteBlob |observable:SQLiteBlobFacet
	observable:SendControlCodeEffect |observable:SendControlCodeEffectFacet
	observable:Software |observable:SoftwareFacet
	observable:StateChangeEffect |observable:StateChangeEffectFacet
	observable:SymbolicLink |observable:SymbolicLinkFacet
	observable:TCPConnection |observable:TCPConnectionFacet
	observable:UNIXAccount |observable:UNIXAccountFacet
	observable:UNIXFilePermissions |observable:UNIXFilePermissionsFacet
	observable:UNIXProcess |observable:UNIXProcessFacet
	observable:UNIXVolume |observable:UNIXVolumeFacet
	observable:URL |observable:URLFacet
	observable:UserAccount |observable:UserAccountFacet
	observable:UserSession |observable:UserSessionFacet
	observable:ValuesEnumeratedEffect |observable:ValuesEnumeratedEffectFacet
	observable:Volume |observable:VolumeFacet
	observable:WhoIs |observable:WhoIsFacet
	observable:WifiAddress |observable:WifiAddressFacet
	observable:WindowsAccount |observable:WindowsAccountFacet
	observable:WindowsActiveDirectoryAccount |observable:WindowsActiveDirectoryAccountFacet
	observable:WindowsComputerSpecification |observable:WindowsComputerSpecificationFacet
	observable:WindowsPEBinaryFile |observable:WindowsPEBinaryFileFacet
	observable:WindowsPrefetch |observable:WindowsPrefetchFacet
	observable:WindowsProcess |observable:WindowsProcessFacet
	observable:WindowsRegistryHive |observable:WindowsRegistryHiveFacet
	observable:WindowsRegistryKey |observable:WindowsRegistryKeyFacet
	observable:WindowsService |observable:WindowsServiceFacet
	observable:WindowsTask |observable:WindowsTaskFacet
	observable:WindowsThread |observable:WindowsThreadFacet
	observable:WindowsVolume |observable:WindowsVolumeFacet
	observable:WirelessNetworkConnection |observable:WirelessNetworkConnectionFacet
	observable:X509Certificate | observable:X509CertificateFacet
	observable:X509V3Extensions | observable:X509V3ExtensionsFacet


### Range Changes (these are changes to the "range" of a property that are not breaking changes: typically these are broadening in the scope of the range)

### Changes (these are general changes to the preexisting ontology that are not breaking or range changes)

### Deprecations/Deletions (classes or properties that were deprecated from the ontology)

* uco-investigation: removed the Investigation namespace (investigation.ttl and investigation-da.ttl) from the UCO ontology - Issue OC-6(https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-6)
* uco-master: removed the Investigation namespace (investigation and investigation-da) imports - Issue OC-6(https://unifiedcyberontology.atlassian.net/jira/software/projects/OC/issues/OC-6)

## Additions

### Class Additions (classes that were added)

### Property Additions (properties that were added)

### Vocabulary Additions/Changes (vocabularies that were added or modified)

## Annotation Changes

