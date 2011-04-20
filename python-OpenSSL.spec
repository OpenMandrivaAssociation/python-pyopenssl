%define pname	OpenSSL
%define name	python-%{pname}
%define version 0.12
%define release %mkrel 1

Summary:	Python interface to the OpenSSL library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://launchpad.net/pyopenssl/main/%{version}/+download/py%{pname}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
Url:		https://launchpad.net/pyopenssl
Requires:	python >= 2.2
BuildRequires:	python-devel openssl-devel
BuildRequires:	tetex-latex tetex-dvipdfm
Obsoletes:	pyOpenSSL
Provides:	pyOpenSSL

%description
pyOpenSSL is a high-level Python wrapper around a subset of OpenSSL library.
It includes SSL Context objects, SSL Connection objects, using Python sockets as a transport layer.

* SSL Context objects;
* SSL Connection objects, that use Python sockets as a transport layer;
* callbacks written in Python;
* an extensive error-handling mechanism that mirrors OpenSSL's error codes;
* and much more.
				
%prep
%__rm -rf %{buildroot}

%setup -q -n py%pname-%version

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

pushd doc
make dvi PAPER=letter
dvipdfm pyOpenSSL.dvi
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO README ChangeLog examples/ doc/pyOpenSSL.pdf
%python_sitearch/*
