%define debug_package %nil
%define pname pyopenssl
%define name python-%{pname}

Summary:	Python interface to the OpenSSL library
Name:		python-%{pname}
Version:	20.0.1
Release:	1
Source0:	https://github.com/pyca/pyopenssl/archive/%{version}/%{name}-%{version}.tar.gz
License:	ASL 2.0
Group:		Development/Python
Url:		https://pyopenssl.org/

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(cryptography)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(sphinx-rtd-theme)

#Obsoletes:	pyOpenSSL
#Provides:	pyOpenSSL
%rename		python-OpenSSL

%description
pyOpenSSL is a high-level Python wrapper around a subset of OpenSSL library.

It includes:
 *   SSL.Connection objects, wrapping the methods of Python's portable sockets;
 *   callbacks written in Python;
 *   an extensive error-handling mechanism, mirroring OpenSSL's error codes;
 *   and much more.

%files
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyOpenSSL-*.egg-info

#--------------------------------------------------------------------

%package doc
Summary:	Documentation for python-%{pname}
BuildArch:	noarch

%description doc
Documentation for python-OpenSSL

%files doc
%doc README.rst INSTALL.rst CHANGELOG.rst doc/_build/html

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%py3_build

# docs
%make_build -C doc html

	
%install
%py3_install
