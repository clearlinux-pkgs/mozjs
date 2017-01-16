#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mozjs
Version  : 24.2.0
Release  : 5
URL      : http://ftp.mozilla.org/pub/js/mozjs-24.2.0.tar.bz2
Source0  : http://ftp.mozilla.org/pub/js/mozjs-24.2.0.tar.bz2
Summary  : A process and system utilities module for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 ICU LGPL-2.0 LGPL-2.1 MIT MPL-2.0-no-copyleft-exception
Requires: mozjs-bin
BuildRequires : nspr-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(x11)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: mozjs24-perl522.patch

%description
ICU is a set of C and C++ libraries that provides robust and full-featured
Unicode and locale support. The library provides calendar support, conversions
for many character sets, language sensitive collation, date
and time formatting, support for many locales, message catalogs
and resources, message formatting, normalization, number and currency
formatting, time zones support, transliteration, word, line and
sentence breaking, etc.

This package contains the Unicode character database and derived
properties, along with converters and time zones data.

This package contains the runtime libraries for ICU. It does
not contain any of the data files needed at runtime and present in the
`icu' and `icu-locales` packages.

%package bin
Summary: bin components for the mozjs package.
Group: Binaries

%description bin
bin components for the mozjs package.


%package dev
Summary: dev components for the mozjs package.
Group: Development
Requires: mozjs-bin
Provides: mozjs-devel

%description dev
dev components for the mozjs package.


%prep
%setup -q -n mozjs-24.2.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484361909

pushd js/src
%configure --disable-static --with-x \
--with-system-zlib \
--enable-system-ffi \
--with-system-nspr
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1484361909

rm -rf %{buildroot}
pushd js/src
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/js24
/usr/bin/js24-config

%files dev
%defattr(-,root,root,-)
/usr/include/mozjs-24/js-config.h
/usr/include/mozjs-24/js.msg
/usr/include/mozjs-24/js/Anchor.h
/usr/include/mozjs-24/js/CallArgs.h
/usr/include/mozjs-24/js/CharacterEncoding.h
/usr/include/mozjs-24/js/Date.h
/usr/include/mozjs-24/js/GCAPI.h
/usr/include/mozjs-24/js/HashTable.h
/usr/include/mozjs-24/js/HeapAPI.h
/usr/include/mozjs-24/js/LegacyIntTypes.h
/usr/include/mozjs-24/js/MemoryMetrics.h
/usr/include/mozjs-24/js/PropertyKey.h
/usr/include/mozjs-24/js/RequiredDefines.h
/usr/include/mozjs-24/js/RootingAPI.h
/usr/include/mozjs-24/js/TemplateLib.h
/usr/include/mozjs-24/js/Utility.h
/usr/include/mozjs-24/js/Value.h
/usr/include/mozjs-24/js/Vector.h
/usr/include/mozjs-24/jsalloc.h
/usr/include/mozjs-24/jsapi.h
/usr/include/mozjs-24/jsclass.h
/usr/include/mozjs-24/jsclist.h
/usr/include/mozjs-24/jscpucfg.h
/usr/include/mozjs-24/jsdbgapi.h
/usr/include/mozjs-24/jsfriendapi.h
/usr/include/mozjs-24/jslock.h
/usr/include/mozjs-24/jsperf.h
/usr/include/mozjs-24/jsprf.h
/usr/include/mozjs-24/jsprototypes.h
/usr/include/mozjs-24/jsproxy.h
/usr/include/mozjs-24/jsprvtd.h
/usr/include/mozjs-24/jspubtd.h
/usr/include/mozjs-24/jstypes.h
/usr/include/mozjs-24/jsutil.h
/usr/include/mozjs-24/jsversion.h
/usr/include/mozjs-24/jswrapper.h
/usr/include/mozjs-24/mozilla/Assertions.h
/usr/include/mozjs-24/mozilla/Atomics.h
/usr/include/mozjs-24/mozilla/Attributes.h
/usr/include/mozjs-24/mozilla/BloomFilter.h
/usr/include/mozjs-24/mozilla/Casting.h
/usr/include/mozjs-24/mozilla/Char16.h
/usr/include/mozjs-24/mozilla/CheckedInt.h
/usr/include/mozjs-24/mozilla/Compiler.h
/usr/include/mozjs-24/mozilla/Constants.h
/usr/include/mozjs-24/mozilla/DebugOnly.h
/usr/include/mozjs-24/mozilla/Decimal.h
/usr/include/mozjs-24/mozilla/Endian.h
/usr/include/mozjs-24/mozilla/EnumSet.h
/usr/include/mozjs-24/mozilla/FloatingPoint.h
/usr/include/mozjs-24/mozilla/GuardObjects.h
/usr/include/mozjs-24/mozilla/HashFunctions.h
/usr/include/mozjs-24/mozilla/Likely.h
/usr/include/mozjs-24/mozilla/LinkedList.h
/usr/include/mozjs-24/mozilla/MSStdInt.h
/usr/include/mozjs-24/mozilla/MathAlgorithms.h
/usr/include/mozjs-24/mozilla/MemoryChecking.h
/usr/include/mozjs-24/mozilla/NullPtr.h
/usr/include/mozjs-24/mozilla/PodOperations.h
/usr/include/mozjs-24/mozilla/Poison.h
/usr/include/mozjs-24/mozilla/Range.h
/usr/include/mozjs-24/mozilla/RangedPtr.h
/usr/include/mozjs-24/mozilla/RefPtr.h
/usr/include/mozjs-24/mozilla/SHA1.h
/usr/include/mozjs-24/mozilla/Scoped.h
/usr/include/mozjs-24/mozilla/SplayTree.h
/usr/include/mozjs-24/mozilla/StandardInteger.h
/usr/include/mozjs-24/mozilla/ThreadLocal.h
/usr/include/mozjs-24/mozilla/TypeTraits.h
/usr/include/mozjs-24/mozilla/TypedEnum.h
/usr/include/mozjs-24/mozilla/Types.h
/usr/include/mozjs-24/mozilla/Util.h
/usr/include/mozjs-24/mozilla/WeakPtr.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc
