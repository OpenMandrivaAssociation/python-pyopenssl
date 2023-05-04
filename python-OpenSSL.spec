%define debug_package %nil
%define pname pyopenssl
%define name python-%{pname}

Summary:	Python interface to the OpenSSL library
Name:		python-%{pname}
Version:	23.1.1
Release:	1
Source0:	https://github.com/pyca/pyopenssl/archive/%{version}/%{pname}-%{version}.tar.gz
License:	LGPLv2
Group:		Development/Python
Url:		https://github.com/pyca/pyopenssl
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-distribute
BuildRequires:	python-pkg-resources
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

%prep
%setup -qn pyopenssl-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyOpenSSL-*.egg-info

%files doc
%doc README.rst INSTALL.rst CHANGELOG.rst
