%define pname	OpenSSL

Summary:	Python interface to the OpenSSL library
Name:		python-%{pname}
Version:	0.12
Release:	4
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
It includes SSL Context objects, SSL Connection objects, using Python sockets as a transport layer.

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


%changelog
* Tue Apr 12 2011 Lev Givon <lev@mandriva.org> 0.12-1mdv2011.0
+ Revision: 652931
- Update to 0.12.

* Tue Feb 08 2011 Lev Givon <lev@mandriva.org> 0.11-1
+ Revision: 636910
- Update to 0.11.

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 0.10-4mdv2011.0
+ Revision: 589930
- rebuild for python 2.7

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.10-3mdv2010.1
+ Revision: 532466
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdv2010.1
+ Revision: 511630
- rebuilt against openssl-0.9.8m

* Fri Jan 08 2010 Emmanuel Andry <eandry@mandriva.org> 0.10-1mdv2010.1
+ Revision: 487797
- New version 0.10

* Sat Sep 19 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.9-1mdv2010.0
+ Revision: 444738
- Updated to 0.9

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.8-1mdv2009.1
+ Revision: 318615
- new release 0.8

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 0.7-2mdv2009.1
+ Revision: 318411
- rebuild for new python

* Sun Aug 17 2008 Lev Givon <lev@mandriva.org> 0.7-1mdv2009.0
+ Revision: 272987
- Update to 0.7.
  Include manual.

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.6-6mdv2009.0
+ Revision: 225137
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Andreas Hasenack <andreas@mandriva.com> 0.6-5mdv2008.1
+ Revision: 116966
- rebuild for new docdir policy (no version in docdir)
- quiet %%setup

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot


* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.6-4mdv2007.0
+ Revision: 88147
- Import python-OpenSSL

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.6-4mdv2007.1
- update file list

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdk
- rebuilt against openssl-0.9.8a

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.6-2mdk
- Rebuild for new python

* Sat Nov 13 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- New release 0.6

* Sun Jun 13 2004 Pascal Terjan <pterjan@mandrake.org> 0.5.1-3mdk
- Fix BuildRequires

* Wed Jun 02 2004 Pascal Terjan <pterjan@mandrake.org> 0.5.1-2mdk
- Respect naming convention
- DIRM

* Wed Apr 21 2004 Pascal Terjan <pterjan@mandrake.org> 0.5.1-1mdk
- First Mandrakelinux version

