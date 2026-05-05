%define debug_package %nil
%define pname pyopenssl
%define name python-%{pname}

Summary:	Python interface to the OpenSSL library
Name:		python-%{pname}
Version:	26.2.0
Release:	1
Source0:	https://github.com/pyca/pyopenssl/archive/%{version}/%{pname}-%{version}.tar.gz
License:	Apache-2.0
Group:		Development/Python
Url:		https://pyopenssl.org/
BuildSystem:	python
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:  noarch
Obsoletes:	pyOpenSSL
Provides:	pyOpenSSL
%rename		python-OpenSSL

%description
pyOpenSSL is a high-level Python wrapper
around a subset of OpenSSL library.

It includes:
* SSL.Connection objects, wrapping the methods of Python's portable sockets;
* callbacks written in Python;
* an extensive error-handling mechanism, mirroring OpenSSL's error codes;
* and much more.

%package doc
Summary:	Documentation for python-%{pname}
BuildArch:	noarch

%description doc
Documentation for python-OpenSSL

%build -p
export CFLAGS="%{optflags} -fno-strict-aliasing"

%files
%license LICENSE
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyopenssl-%{version}.dist-info

%files doc
%doc README.rst INSTALL.rst CHANGELOG.rst
