#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Filters to enhance web typography, including support for Django & Jinja templates
Summary(pl.UTF-8):	Filtry rozszerzające typografię WWW z obsługą szablonów Django i Jinja
Name:		python-typogrify
Version:	2.0.7
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/typogrify/
Source0:	https://files.pythonhosted.org/packages/source/t/typogrify/typogrify-%{version}.tar.gz
# Source0-md5:	63f38f80531996f187d2894cc497ba08
URL:		https://pypi.org/project/typogrify/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Typogrify provides a set of custom filters that automatically apply
various transformations to plain text in order to yield
typographically-improved HTML. While often used in conjunction with
Jinja and Django template systems, the filters can be used in any
environment.

%description -l pl.UTF-8
Typogrify udostępnia zestaw dostosowanych filtrów, automatycznie
nakładających na czysty tekst różne przekształcenia, aby wytworzyć
typograficznie ulepszony HTML. Filtry zwykle używane są wraz z
systemami szablonów Jinja i Django, ale można ich używać w dowolnym
środowisku.

%package -n python3-typogrify
Summary:	Filters to enhance web typography, including support for Django & Jinja templates
Summary(pl.UTF-8):	Filtry rozszerzające typografię WWW z obsługą szablonów Django i Jinja
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-typogrify
Typogrify provides a set of custom filters that automatically apply
various transformations to plain text in order to yield
typographically-improved HTML. While often used in conjunction with
Jinja and Django template systems, the filters can be used in any
environment.

%description -n python3-typogrify -l pl.UTF-8
Typogrify udostępnia zestaw dostosowanych filtrów, automatycznie
nakładających na czysty tekst różne przekształcenia, aby wytworzyć
typograficznie ulepszony HTML. Filtry zwykle używane są wraz z
systemami szablonów Jinja i Django, ale można ich używać w dowolnym
środowisku.

%prep
%setup -q -n typogrify-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/typogrify
%{py_sitescriptdir}/typogrify-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-typogrify
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/typogrify
%{py3_sitescriptdir}/typogrify-%{version}-py*.egg-info
%endif
