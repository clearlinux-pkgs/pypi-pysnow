#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pysnow
Version  : 0.7.17
Release  : 10
URL      : https://files.pythonhosted.org/packages/d4/64/c958b786efe31b5b23777501a23be8e777a10e7dc0213f1b7a85f3d84d15/pysnow-0.7.17.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/64/c958b786efe31b5b23777501a23be8e777a10e7dc0213f1b7a85f3d84d15/pysnow-0.7.17.tar.gz
Summary  : ServiceNow HTTP client library
Group    : Development/Tools
License  : MIT
Requires: pypi-pysnow-license = %{version}-%{release}
Requires: pypi-pysnow-python = %{version}-%{release}
Requires: pypi-pysnow-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry)

%description
```
______   __  __    ______    __   __    ______    __     __
/\  == \ /\ \_\ \  /\  ___\  /\ "-.\ \  /\  __ \  /\ \  _ \ \
\ \  _-/ \ \____ \ \ \___  \ \ \ \-.  \ \ \ \/\ \ \ \ \/ ".\ \
\ \_\    \/\_____\ \/\_____\ \ \_\\"\_\ \ \_____\ \ \__/".~\_\
\/_/     \/_____/  \/_____/  \/_/ \/_/  \/_____/  \/_/   \/_/
- Python library for ServiceNow
```

%package license
Summary: license components for the pypi-pysnow package.
Group: Default

%description license
license components for the pypi-pysnow package.


%package python
Summary: python components for the pypi-pysnow package.
Group: Default
Requires: pypi-pysnow-python3 = %{version}-%{release}

%description python
python components for the pypi-pysnow package.


%package python3
Summary: python3 components for the pypi-pysnow package.
Group: Default
Requires: python3-core
Provides: pypi(pysnow)
Requires: pypi(ijson)
Requires: pypi(oauthlib)
Requires: pypi(python_magic)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(requests_oauthlib)
Requires: pypi(six)

%description python3
python3 components for the pypi-pysnow package.


%prep
%setup -q -n pysnow-0.7.17
cd %{_builddir}/pysnow-0.7.17
pushd ..
cp -a pysnow-0.7.17 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656400286
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . ijson
pypi-dep-fix.py . pytz
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . ijson
pypi-dep-fix.py . pytz
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pysnow
cp %{_builddir}/pysnow-0.7.17/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pysnow/a7321f7a85044bafc110dd42eb1ea314fe374dcc
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} ijson
pypi-dep-fix.py %{buildroot} pytz
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pysnow/a7321f7a85044bafc110dd42eb1ea314fe374dcc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
