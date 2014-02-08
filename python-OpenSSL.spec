%define pname	OpenSSL

Summary:	Python interface to the OpenSSL library
Name:		python-%{pname}
Version:	0.12
Release:	6
Source:		http://launchpad.net/pyopenssl/main/%{version}/+download/py%{pname}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Development/Python
Url:		https://launchpad.net/pyopenssl
Requires:	python >= 2.2
BuildRequires:	python-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvipdfm
# We don't need whole texlive collection
# but it's hard to find what exactly we need
# so we require whole set for now
BuildRequires:	texlive
Provides:	pyOpenSSL

%description
pyOpenSSL is a high-level Python wrapper around a subset of OpenSSL library.
It includes SSL Context objects, SSL Connection objects, using Python
sockets as a transport layer.

* SSL Context objects;
* SSL Connection objects, that use Python sockets as a transport layer;
* callbacks written in Python;
* an extensive error-handling mechanism that mirrors OpenSSL's error codes;
* and much more.
				
%prep
%setup -q -n py%{pname}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

pushd doc
make dvi PAPER=letter
dvipdfm pyOpenSSL.dvi
popd

%files
%doc TODO README ChangeLog examples/ doc/pyOpenSSL.pdf
%{python_sitearch}/*


