#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : qt6grpc
Version  : 6.7.3
Release  : 24
URL      : https://download.qt.io/official_releases/qt/6.7/6.7.3/submodules/qtgrpc-everywhere-src-6.7.3.zip
Source0  : https://download.qt.io/official_releases/qt/6.7/6.7.3/submodules/qtgrpc-everywhere-src-6.7.3.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6grpc-lib = %{version}-%{release}
Requires: qt6grpc-libexec = %{version}-%{release}
Requires: qt6grpc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : protobuf-dev
BuildRequires : protobuf-staticdev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
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
%setup -q -n qtgrpc-everywhere-src-6.7.3
cd %{_builddir}/qtgrpc-everywhere-src-6.7.3
pushd ..
cp -a qtgrpc-everywhere-src-6.7.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727893511
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
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1727893511
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6grpc
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6grpc/1c619b057a9bf7a8234b3105fcfb5b375e749db1 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6grpc/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6grpc/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/LicenseRef-protobuf.txt %{buildroot}/usr/share/package-licenses/qt6grpc/57919d5bf210193d05ba496a870832582f475559 || :
cp %{_builddir}/qtgrpc-everywhere-src-%{version}/LICENSES/LicenseRef-protobuf.txt %{buildroot}/usr/share/package-licenses/qt6grpc/57919d5bf210193d05ba496a870832582f475559 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtGrpc/6.7.3/QtGrpc/private/qabstractgrpcchannel_p.h
/usr/include/QtGrpc/6.7.3/QtGrpc/private/qgrpcclientinterceptormanager_p.h
/usr/include/QtGrpc/6.7.3/QtGrpc/private/qtgrpc-config_p.h
/usr/include/QtGrpc/6.7.3/QtGrpc/private/qtgrpcglobal_p.h
/usr/include/QtGrpc/QAbstractGrpcChannel
/usr/include/QtGrpc/QAbstractGrpcClient
/usr/include/QtGrpc/QGrpcBidirStream
/usr/include/QtGrpc/QGrpcCallOptions
/usr/include/QtGrpc/QGrpcCallReply
/usr/include/QtGrpc/QGrpcChannelOperation
/usr/include/QtGrpc/QGrpcChannelOptions
/usr/include/QtGrpc/QGrpcClientInterceptor
/usr/include/QtGrpc/QGrpcClientInterceptorManager
/usr/include/QtGrpc/QGrpcClientStream
/usr/include/QtGrpc/QGrpcHttp2Channel
/usr/include/QtGrpc/QGrpcInterceptorContinuation
/usr/include/QtGrpc/QGrpcMetadata
/usr/include/QtGrpc/QGrpcOperation
/usr/include/QtGrpc/QGrpcRpcInfo
/usr/include/QtGrpc/QGrpcServerStream
/usr/include/QtGrpc/QGrpcStatus
/usr/include/QtGrpc/QtGrpc
/usr/include/QtGrpc/QtGrpcDepends
/usr/include/QtGrpc/QtGrpcVersion
/usr/include/QtGrpc/qabstractgrpcchannel.h
/usr/include/QtGrpc/qabstractgrpcclient.h
/usr/include/QtGrpc/qgrpccalloptions.h
/usr/include/QtGrpc/qgrpccallreply.h
/usr/include/QtGrpc/qgrpcchanneloperation.h
/usr/include/QtGrpc/qgrpcchanneloptions.h
/usr/include/QtGrpc/qgrpcclientinterceptor.h
/usr/include/QtGrpc/qgrpcclientinterceptormanager.h
/usr/include/QtGrpc/qgrpchttp2channel.h
/usr/include/QtGrpc/qgrpcmetadata.h
/usr/include/QtGrpc/qgrpcoperation.h
/usr/include/QtGrpc/qgrpcstatus.h
/usr/include/QtGrpc/qgrpcstream.h
/usr/include/QtGrpc/qtgrpc-config.h
/usr/include/QtGrpc/qtgrpcexports.h
/usr/include/QtGrpc/qtgrpcglobal.h
/usr/include/QtGrpc/qtgrpcversion.h
/usr/include/QtGrpcQuick/6.7.3/QtGrpcQuick/private/qqmlgrpccalloptions_p.h
/usr/include/QtGrpcQuick/6.7.3/QtGrpcQuick/private/qqmlgrpcchanneloptions_p.h
/usr/include/QtGrpcQuick/6.7.3/QtGrpcQuick/private/qqmlgrpchttp2channel_p.h
/usr/include/QtGrpcQuick/6.7.3/QtGrpcQuick/private/qqmlgrpcmetadata_p.h
/usr/include/QtGrpcQuick/QQmlAbstractGrpcChannel
/usr/include/QtGrpcQuick/QtGrpcQuick
/usr/include/QtGrpcQuick/QtGrpcQuickDepends
/usr/include/QtGrpcQuick/QtGrpcQuickVersion
/usr/include/QtGrpcQuick/qqmlabstractgrpcchannel.h
/usr/include/QtGrpcQuick/qtgrpcquickexports.h
/usr/include/QtGrpcQuick/qtgrpcquickversion.h
/usr/include/QtProtobuf/6.7.3/QtProtobuf/private/qprotobufmessage_p.h
/usr/include/QtProtobuf/6.7.3/QtProtobuf/private/qprotobufselfcheckiterator_p.h
/usr/include/QtProtobuf/6.7.3/QtProtobuf/private/qprotobufserializer_p.h
/usr/include/QtProtobuf/6.7.3/QtProtobuf/private/qtprotobuf-config_p.h
/usr/include/QtProtobuf/6.7.3/QtProtobuf/private/qtprotobuflogging_p.h
/usr/include/QtProtobuf/QAbstractProtobufSerializer
/usr/include/QtProtobuf/QProtobufBaseSerializer
/usr/include/QtProtobuf/QProtobufJsonSerializer
/usr/include/QtProtobuf/QProtobufMessage
/usr/include/QtProtobuf/QProtobufMessageDeleter
/usr/include/QtProtobuf/QProtobufOneof
/usr/include/QtProtobuf/QProtobufSerializer
/usr/include/QtProtobuf/QtProtobuf
/usr/include/QtProtobuf/QtProtobufDepends
/usr/include/QtProtobuf/QtProtobufVersion
/usr/include/QtProtobuf/qabstractprotobufserializer.h
/usr/include/QtProtobuf/qprotobufbaseserializer.h
/usr/include/QtProtobuf/qprotobufjsonserializer.h
/usr/include/QtProtobuf/qprotobuflazymessagepointer.h
/usr/include/QtProtobuf/qprotobufmessage.h
/usr/include/QtProtobuf/qprotobufobject.h
/usr/include/QtProtobuf/qprotobufoneof.h
/usr/include/QtProtobuf/qprotobufserializer.h
/usr/include/QtProtobuf/qtprotobuf-config.h
/usr/include/QtProtobuf/qtprotobufexports.h
/usr/include/QtProtobuf/qtprotobufglobal.h
/usr/include/QtProtobuf/qtprotobuftypes.h
/usr/include/QtProtobuf/qtprotobufversion.h
/usr/include/QtProtobufQtCoreTypes/6.7.3/QtProtobufQtCoreTypes/private/QtCore.qpb.h
/usr/include/QtProtobufQtCoreTypes/6.7.3/QtProtobufQtCoreTypes/private/protobufqtcoretypes_exports.qpb.h
/usr/include/QtProtobufQtCoreTypes/6.7.3/QtProtobufQtCoreTypes/private/qtprotobufqttypescommon_p.h
/usr/include/QtProtobufQtCoreTypes/QtCore/QtCore.proto
/usr/include/QtProtobufQtCoreTypes/QtProtobufQtCoreTypes
/usr/include/QtProtobufQtCoreTypes/QtProtobufQtCoreTypesDepends
/usr/include/QtProtobufQtCoreTypes/QtProtobufQtCoreTypesVersion
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypes.h
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypesexports.h
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypesglobal.h
/usr/include/QtProtobufQtCoreTypes/qtprotobufqtcoretypesversion.h
/usr/include/QtProtobufQtGuiTypes/6.7.3/QtProtobufQtGuiTypes/private/QtGui.qpb.h
/usr/include/QtProtobufQtGuiTypes/6.7.3/QtProtobufQtGuiTypes/private/protobufqtguitypes_exports.qpb.h
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
/usr/include/QtProtobufWellKnownTypes/api.qpb.h
/usr/include/QtProtobufWellKnownTypes/duration.qpb.h
/usr/include/QtProtobufWellKnownTypes/empty.qpb.h
/usr/include/QtProtobufWellKnownTypes/field_mask.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/any.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/api.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/duration.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/empty.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/field_mask.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/protobufwellknowntypes_exports.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/source_context.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/struct.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/timestamp.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/type.qpb.h
/usr/include/QtProtobufWellKnownTypes/google/protobuf/wrappers.qpb.h
/usr/include/QtProtobufWellKnownTypes/protobufwellknowntypes_exports.qpb.h
/usr/include/QtProtobufWellKnownTypes/qprotobufanysupport.h
/usr/include/QtProtobufWellKnownTypes/qtprotobufwellknowntypesexports.h
/usr/include/QtProtobufWellKnownTypes/qtprotobufwellknowntypesglobal.h
/usr/include/QtProtobufWellKnownTypes/qtprotobufwellknowntypesversion.h
/usr/include/QtProtobufWellKnownTypes/source_context.qpb.h
/usr/include/QtProtobufWellKnownTypes/struct.qpb.h
/usr/include/QtProtobufWellKnownTypes/timestamp.qpb.h
/usr/include/QtProtobufWellKnownTypes/type.qpb.h
/usr/include/QtProtobufWellKnownTypes/wrappers.qpb.h
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
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickConfig.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickConfigVersion.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickDependencies.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickTargets.cmake
/usr/lib64/cmake/Qt6GrpcQuick/Qt6GrpcQuickVersionlessTargets.cmake
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
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickpluginTargets.cmake
/usr/lib64/libQt6Grpc.prl
/usr/lib64/libQt6Grpc.so
/usr/lib64/libQt6GrpcQuick.prl
/usr/lib64/libQt6GrpcQuick.so
/usr/lib64/libQt6Protobuf.prl
/usr/lib64/libQt6Protobuf.so
/usr/lib64/libQt6ProtobufQtCoreTypes.prl
/usr/lib64/libQt6ProtobufQtCoreTypes.so
/usr/lib64/libQt6ProtobufQtGuiTypes.prl
/usr/lib64/libQt6ProtobufQtGuiTypes.so
/usr/lib64/libQt6ProtobufWellKnownTypes.prl
/usr/lib64/libQt6ProtobufWellKnownTypes.so
/usr/lib64/pkgconfig/Qt6Grpc.pc
/usr/lib64/pkgconfig/Qt6GrpcQuick.pc
/usr/lib64/pkgconfig/Qt6Protobuf.pc
/usr/lib64/pkgconfig/Qt6ProtobufQtCoreTypes.pc
/usr/lib64/pkgconfig/Qt6ProtobufQtGuiTypes.pc
/usr/lib64/pkgconfig/Qt6ProtobufWellKnownTypes.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_grpc.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_grpc_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_grpcquick.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_grpcquick_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobuf.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobuf_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtcoretypes.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtcoretypes_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtguitypes.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufqtguitypes_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufwellknowntypes.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_protobufwellknowntypes_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Grpc.so.6.7.3
/V3/usr/lib64/libQt6GrpcQuick.so.6.7.3
/V3/usr/lib64/libQt6Protobuf.so.6.7.3
/V3/usr/lib64/libQt6ProtobufQtCoreTypes.so.6.7.3
/V3/usr/lib64/libQt6ProtobufQtGuiTypes.so.6.7.3
/V3/usr/lib64/libQt6ProtobufWellKnownTypes.so.6.7.3
/V3/usr/lib64/qt6/qml/QtGrpc/libgrpcquickplugin.so
/usr/lib64/libQt6Grpc.so.6
/usr/lib64/libQt6Grpc.so.6.7.3
/usr/lib64/libQt6GrpcQuick.so.6
/usr/lib64/libQt6GrpcQuick.so.6.7.3
/usr/lib64/libQt6Protobuf.so.6
/usr/lib64/libQt6Protobuf.so.6.7.3
/usr/lib64/libQt6ProtobufQtCoreTypes.so.6
/usr/lib64/libQt6ProtobufQtCoreTypes.so.6.7.3
/usr/lib64/libQt6ProtobufQtGuiTypes.so.6
/usr/lib64/libQt6ProtobufQtGuiTypes.so.6.7.3
/usr/lib64/libQt6ProtobufWellKnownTypes.so.6
/usr/lib64/libQt6ProtobufWellKnownTypes.so.6.7.3
/usr/lib64/qt6/metatypes/qt6grpc_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6grpcquick_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobuf_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobufqtcoretypes_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobufqtguitypes_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6protobufwellknowntypes_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/Grpc.json
/usr/lib64/qt6/modules/GrpcQuick.json
/usr/lib64/qt6/modules/Protobuf.json
/usr/lib64/qt6/modules/ProtobufQtCoreTypes.json
/usr/lib64/qt6/modules/ProtobufQtGuiTypes.json
/usr/lib64/qt6/modules/ProtobufWellKnownTypes.json
/usr/lib64/qt6/qml/QtGrpc/libgrpcquickplugin.so
/usr/lib64/qt6/qml/QtGrpc/plugins.qmltypes
/usr/lib64/qt6/qml/QtGrpc/qmldir

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/qtgrpcgen
/V3/usr/libexec/qtprotobufgen
/usr/libexec/qtgrpcgen
/usr/libexec/qtprotobufgen

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6grpc/1c619b057a9bf7a8234b3105fcfb5b375e749db1
/usr/share/package-licenses/qt6grpc/57919d5bf210193d05ba496a870832582f475559
/usr/share/package-licenses/qt6grpc/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6grpc/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6grpc/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6grpc/dc8f2e570bf431427dbc3bab9d4d551b53a60208
