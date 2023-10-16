#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : qt6grpc
Version  : 6.6.0
Release  : 3
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.0/submodules/qtgrpc-everywhere-src-6.6.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.0/submodules/qtgrpc-everywhere-src-6.6.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6grpc-lib = %{version}-%{release}
Requires: qt6grpc-libexec = %{version}-%{release}
Requires: qt6grpc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : protobuf-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6grpc package.
Group: Development
Requires: qt6grpc-lib = %{version}-%{release}
Provides: qt6grpc-devel = %{version}-%{release}
Requires: qt6grpc = %{version}-%{release}

%description dev
dev components for the qt6grpc package.


%package lib
Summary: lib components for the qt6grpc package.
Group: Libraries
Requires: qt6grpc-libexec = %{version}-%{release}
Requires: qt6grpc-license = %{version}-%{release}

%description lib
lib components for the qt6grpc package.


%package libexec
Summary: libexec components for the qt6grpc package.
Group: Default
Requires: qt6grpc-license = %{version}-%{release}

%description libexec
libexec components for the qt6grpc package.


%package license
Summary: license components for the qt6grpc package.
Group: Default

%description license
license components for the qt6grpc package.


%prep
%setup -q -n qtgrpc-everywhere-src-6.6.0
cd %{_builddir}/qtgrpc-everywhere-src-6.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697483436
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697483436
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6grpc
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6grpc/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6grpc_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobuf_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobufqtcoretypes_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobufqtguitypes_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobufwellknowntypes_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_grpc.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_grpc_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobuf.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobuf_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtcoretypes.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtcoretypes_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtguitypes.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtguitypes_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufwellknowntypes.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufwellknowntypes_private.pri
/usr/lib64/qt6/modules/Grpc.json
/usr/lib64/qt6/modules/Protobuf.json
/usr/lib64/qt6/modules/ProtobufQtCoreTypes.json
/usr/lib64/qt6/modules/ProtobufQtGuiTypes.json
/usr/lib64/qt6/modules/ProtobufWellKnownTypes.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtGrpc/6.6.0/QtGrpc/private/qabstractgrpcchannel_p.h
/usr/include/QtGrpc/6.6.0/QtGrpc/private/qtgrpc-config_p.h
/usr/include/QtGrpc/6.6.0/QtGrpc/private/qtgrpcglobal_p.h
/usr/include/QtGrpc/QAbstractGrpcChannel
/usr/include/QtGrpc/QAbstractGrpcClient
/usr/include/QtGrpc/QGrpcCallOptions
/usr/include/QtGrpc/QGrpcCallReply
/usr/include/QtGrpc/QGrpcChannelOptions
/usr/include/QtGrpc/QGrpcHttp2Channel
/usr/include/QtGrpc/QGrpcMetadata
/usr/include/QtGrpc/QGrpcOperation
/usr/include/QtGrpc/QGrpcStatus
/usr/include/QtGrpc/QGrpcStream
/usr/include/QtGrpc/QtGrpc
/usr/include/QtGrpc/QtGrpcDepends
/usr/include/QtGrpc/QtGrpcVersion
/usr/include/QtGrpc/qabstractgrpcchannel.h
/usr/include/QtGrpc/qabstractgrpcclient.h
/usr/include/QtGrpc/qgrpccalloptions.h
/usr/include/QtGrpc/qgrpccallreply.h
/usr/include/QtGrpc/qgrpcchanneloptions.h
/usr/include/QtGrpc/qgrpchttp2channel.h
/usr/include/QtGrpc/qgrpcmetadata.h
/usr/include/QtGrpc/qgrpcoperation.h
/usr/include/QtGrpc/qgrpcstatus.h
/usr/include/QtGrpc/qgrpcstream.h
/usr/include/QtGrpc/qtgrpc-config.h
/usr/include/QtGrpc/qtgrpcexports.h
/usr/include/QtGrpc/qtgrpcglobal.h
/usr/include/QtGrpc/qtgrpcversion.h
/usr/include/QtProtobuf/6.6.0/QtProtobuf/private/qprotobufmessage_p.h
/usr/include/QtProtobuf/6.6.0/QtProtobuf/private/qprotobufserializer_p.h
/usr/include/QtProtobuf/6.6.0/QtProtobuf/private/qtprotobuf-config_p.h
/usr/include/QtProtobuf/6.6.0/QtProtobuf/private/qtprotobuflogging_p.h
/usr/include/QtProtobuf/QAbstractProtobufSerializer
/usr/include/QtProtobuf/QProtobufMessage
/usr/include/QtProtobuf/QProtobufMessageDeleter
/usr/include/QtProtobuf/QProtobufOneof
/usr/include/QtProtobuf/QProtobufSerializer
/usr/include/QtProtobuf/QtProtobuf
/usr/include/QtProtobuf/QtProtobufDepends
/usr/include/QtProtobuf/QtProtobufVersion
/usr/include/QtProtobuf/qabstractprotobufserializer.h
/usr/include/QtProtobuf/qprotobuflazymessagepointer.h
/usr/include/QtProtobuf/qprotobufmessage.h
/usr/include/QtProtobuf/qprotobufobject.h
/usr/include/QtProtobuf/qprotobufoneof.h
/usr/include/QtProtobuf/qprotobufselfcheckiterator.h
/usr/include/QtProtobuf/qprotobufserializer.h
/usr/include/QtProtobuf/qtprotobuf-config.h
/usr/include/QtProtobuf/qtprotobufexports.h
/usr/include/QtProtobuf/qtprotobufglobal.h
/usr/include/QtProtobuf/qtprotobuftypes.h
/usr/include/QtProtobuf/qtprotobufversion.h
/usr/include/QtProtobufQtCoreTypes/6.6.0/QtProtobufQtCoreTypes/private/QtCore.qpb.h
/usr/include/QtProtobufQtCoreTypes/6.6.0/QtProtobufQtCoreTypes/private/qtprotobufqttypescommon_p.h
/usr/include/QtProtobufQtCoreTypes/QtCore/QtCore.proto
/usr/include/QtProtobufQtCoreTypes/QtProtobufQtCoreTypes
/usr/include/QtProtobufQtCoreTypes/QtProtobufQtCoreTypesDepends
/usr/include/QtProtobufQtCoreTypes/QtProtobufQtCoreTypesVersion
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypes.h
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypesexports.h
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypesglobal.h
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypesversion.h
/usr/include/QtProtobufQtGuiTypes/6.6.0/QtProtobufQtGuiTypes/private/QtGui.qpb.h
/usr/include/QtProtobufQtGuiTypes/QtGui/QtGui.proto
/usr/include/QtProtobufQtGuiTypes/QtProtobufQtGuiTypes
/usr/include/QtProtobufQtGuiTypes/QtProtobufQtGuiTypesDepends
/usr/include/QtProtobufQtGuiTypes/QtProtobufQtGuiTypesVersion
/usr/include/QtProtobufQtGuiTypes/qtprotobufqtguitypes.h
/usr/include/QtProtobufQtGuiTypes/qtprotobufqtguitypesexports.h
/usr/include/QtProtobufQtGuiTypes/qtprotobufqtguitypesglobal.h
/usr/include/QtProtobufQtGuiTypes/qtprotobufqtguitypesversion.h
/usr/include/QtProtobufWellKnownTypes/QtProtobufWellKnownTypes
/usr/include/QtProtobufWellKnownTypes/QtProtobufWellKnownTypesDepends
/usr/include/QtProtobufWellKnownTypes/QtProtobufWellKnownTypesVersion
/usr/include/QtProtobufWellKnownTypes/any.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/any.qpb.h
/usr/include/QtProtobufWellKnownTypes/qprotobufanysupport.h
/usr/include/QtProtobufWellKnownTypes/qtprotobufwellknowntypesexports.h
/usr/include/QtProtobufWellKnownTypes/qtprotobufwellknowntypesglobal.h
/usr/include/QtProtobufWellKnownTypes/qtprotobufwellknowntypesversion.h
/usr/lib64/cmake/Qt6/FindWrapProtobuf.cmake
/usr/lib64/cmake/Qt6/FindWrapProtoc.cmake
/usr/lib64/cmake/Qt6/FindWrapgRPC.cmake
/usr/lib64/cmake/Qt6/FindWrapgRPCPlugin.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtGrpcTestsConfig.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcConfig.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcConfigVersion.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcDependencies.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcTargets.cmake
/usr/lib64/cmake/Qt6Grpc/Qt6GrpcVersionlessTargets.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsConfig.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsDependencies.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsMacros.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsTargets.cmake
/usr/lib64/cmake/Qt6GrpcTools/Qt6GrpcToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufBuildInternals.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufConfig.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufConfigVersion.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufDependencies.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufTargets.cmake
/usr/lib64/cmake/Qt6Protobuf/Qt6ProtobufVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Protobuf/QtProtobufProperties.cmake.in
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesConfig.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesConfigVersion.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesDependencies.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesProtobufProperties.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesTargets.cmake
/usr/lib64/cmake/Qt6ProtobufQtCoreTypes/Qt6ProtobufQtCoreTypesVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesConfig.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesConfigVersion.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesDependencies.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesProtobufProperties.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesTargets.cmake
/usr/lib64/cmake/Qt6ProtobufQtGuiTypes/Qt6ProtobufQtGuiTypesVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsConfig.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsDependencies.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsMacros.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsTargets.cmake
/usr/lib64/cmake/Qt6ProtobufTools/Qt6ProtobufToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ProtobufTools/QtProtocCommandWrapper.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesBuildInternals.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesConfig.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesConfigVersion.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesDependencies.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesTargets.cmake
/usr/lib64/cmake/Qt6ProtobufWellKnownTypes/Qt6ProtobufWellKnownTypesVersionlessTargets.cmake
/usr/lib64/libQt6Grpc.prl
/usr/lib64/libQt6Grpc.so
/usr/lib64/libQt6Protobuf.prl
/usr/lib64/libQt6Protobuf.so
/usr/lib64/libQt6ProtobufQtCoreTypes.prl
/usr/lib64/libQt6ProtobufQtCoreTypes.so
/usr/lib64/libQt6ProtobufQtGuiTypes.prl
/usr/lib64/libQt6ProtobufQtGuiTypes.so
/usr/lib64/libQt6ProtobufWellKnownTypes.prl
/usr/lib64/libQt6ProtobufWellKnownTypes.so
/usr/lib64/pkgconfig/Qt6Grpc.pc
/usr/lib64/pkgconfig/Qt6Protobuf.pc
/usr/lib64/pkgconfig/Qt6ProtobufQtCoreTypes.pc
/usr/lib64/pkgconfig/Qt6ProtobufQtGuiTypes.pc
/usr/lib64/pkgconfig/Qt6ProtobufWellKnownTypes.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6Grpc.so.6
/usr/lib64/libQt6Grpc.so.6.6.0
/usr/lib64/libQt6Protobuf.so.6
/usr/lib64/libQt6Protobuf.so.6.6.0
/usr/lib64/libQt6ProtobufQtCoreTypes.so.6
/usr/lib64/libQt6ProtobufQtCoreTypes.so.6.6.0
/usr/lib64/libQt6ProtobufQtGuiTypes.so.6
/usr/lib64/libQt6ProtobufQtGuiTypes.so.6.6.0
/usr/lib64/libQt6ProtobufWellKnownTypes.so.6
/usr/lib64/libQt6ProtobufWellKnownTypes.so.6.6.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/qtgrpcgen
/usr/libexec/qtprotobufgen

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6grpc/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6grpc/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6grpc/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6grpc/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6grpc/f45ee1c765646813b442ca58de72e20a64a7ddba
