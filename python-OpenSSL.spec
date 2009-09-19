%define pname OpenSSL
%define name python-%{pname}
%define version 0.9
%define release %mkrel 1

Summary: Python interface to the OpenSSL library
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://telia.dl.sourceforge.net/sourceforge/pyopenssl/py%pname-%{version}.tar.gz
License: LGPLv2
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://pyopenssl.sourceforge.net/
Requires: python >= 2.2
BuildRequires: python-devel openssl-devel
BuildRequires: tetex-latex tetex-dvipdfm
Obsoletes: pyOpenSSL
Provides: pyOpenSSL

%description
pyOpenSSL is a high-level Python wrapper around a subset of OpenSSL library.
It includes

* SSL.Connection objects, wrapping the methods of Python's portable sockets;
* callbacks written in Python;
* an extensive error-handling mechanism, mirroring OpenSSL's error codes;
* and much more.
				
%prep
%__rm -rf %{buildroot}

%setup -q -n py%pname-%version

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --record=FILELIST

pushd doc
make dvi PAPER=letter
dvipdfm pyOpenSSL.dvi
popd

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc COPYING TODO README INSTALL ChangeLog examples/ doc/pyOpenSSL.pdf


