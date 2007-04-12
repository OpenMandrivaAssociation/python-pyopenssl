%define pname OpenSSL
%define name python-%{pname}
%define version 0.6
%define release %mkrel 4

Summary: Python interface to the OpenSSL library.
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://telia.dl.sourceforge.net/sourceforge/pyopenssl/py%pname-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://pyopenssl.sourceforge.net/
Requires: python >= 2.2
BuildRequires: python-devel openssl-devel
Obsoletes: pyOpenSSL
Provides: pyOpenSSL

%description
High-level wrapper around a subset of the OpenSSL library, includes
 * SSL.Connection objects, wrapping the methods of Python's portable sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes
...  and much more ;)
				
%prep
rm -rf $RPM_BUILD_ROOT

%setup -n py%pname-%version

%build
%_bindir/python setup.py build

%install
%_bindir/python setup.py install --root=$RPM_BUILD_ROOT 
chmod 0644 examples/SecureXMLRPCServer.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING TODO README INSTALL ChangeLog examples
%py_platsitedir/*SSL*


