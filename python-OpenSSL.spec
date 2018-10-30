%define debug_package %nil
%define pname pyopenssl
%define name python-%{pname}

Summary:	Python interface to the OpenSSL library
Name:		python-%{pname}
Version:	16.2.0
Release:	3
Source0:	http://launchpad.net/pyopenssl/main/%{version}/+download/pyOpenSSL-%{version}.tar.gz
License:	LGPLv2
Group:		Development/Python
Url:		https://launchpad.net/pyopenssl
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-distribute
BuildRequires:	python-pkg-resources
BuildRequires:	python2-distribute
BuildRequires:	python2-pkg-resources
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

%package -n python2-%{pname}
Summary:	Python wrapper module around the OpenSSL library
Group:		Development/Python

%description -n python2-%{pname}
High-level wrapper around a subset of
the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes


%package doc
Summary:	Documentation for python-%{pname}
BuildArch:	noarch

%description doc
Documentation for python-OpenSSL

%prep
%setup -qn pyOpenSSL-%{version}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python} setup.py build

pushd %{py2dir}
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python2} setup.py build
popd

%install
%{__python} setup.py install --skip-build --root %{buildroot}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd


%files
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyOpenSSL-*.egg-info


%files -n python2-%{pname}
%{python2_sitelib}/OpenSSL/
%{python2_sitelib}/pyOpenSSL-*.egg-info

%files doc
%doc README.rst INSTALL.rst CHANGELOG.rst examples/
