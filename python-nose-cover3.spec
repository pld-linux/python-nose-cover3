#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Coverage 3.x support for Nose
Summary(pl.UTF-8):	Obsługa Coverage 3.x dla Nose
Name:		python-nose-cover3
Version:	0.1.0
Release:	3
License:	LGPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nose-cover3/
Source0:	https://files.pythonhosted.org/packages/source/n/nose-cover3/nose-cover3-%{version}.tar.gz
# Source0-md5:	82f981eaa007b430679899256050fa0c
Patch0:		nose-cover3-no-2to3.patch
URL:		https://pypi.org/project/nose-cover3/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
Requires:	python-nose
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coverage 3.x support for Nose.

%description -l pl.UTF-8
Obsługa Coverage 3.x dla Nose.

%package -n python3-nose-cover3
Summary:	Coverage 3.x support for Nose
Summary(pl.UTF-8):	Obsługa Coverage 3.x dla Nose
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-nose

%description -n python3-nose-cover3
Coverage 3.x support for Nose.

%description -n python3-nose-cover3 -l pl.UTF-8
Obsługa Coverage 3.x dla Nose.

%prep
%setup -q -n nose-cover3-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
# setuptools no longer support use_2to3, do it manually
2to3-%{py3_ver} -n -w -o build-3/lib/nosecover3 nosecover3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/nosecover3
%{py_sitescriptdir}/nose_cover3-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nose-cover3
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/nosecover3
%{py3_sitescriptdir}/nose_cover3-%{version}-py*.egg-info
%endif
