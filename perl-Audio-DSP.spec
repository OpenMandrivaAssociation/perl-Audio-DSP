%define upstream_name	 Audio-DSP
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl interface to OSS digital audio device
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Audio/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Audio-DSP-0.02-VOCP.patch

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Audio::DSP is built around the OSS (Open Sound System) API and allows perl to
interface with a digital audio device. It provides, among other things, an
initialization method which opens and handles ioctl messaging on the audio
device file. Audio::DSP also provides some rudimentary methods for the storage
and manipulation of audio data in memory.

In order to use Audio::DSP, you'll need to have the necessary OSS
drivers/libraries installed. OSS is available for many popular Unices, and a
GPLed version (with which this extension was initially developed and tested) is
distributed with with the Linux kernel. 

%prep

%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
# doesn't work

%install
%{__rm} -rf %{buildroot} 
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{perl_vendorarch}/Audio
%{perl_vendorarch}/auto/Audio
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.20.0-3
+ Revision: 680482
- mass rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 555423
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 402983
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-13mdv2009.0
+ Revision: 255345
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.02-11mdv2008.1
+ Revision: 151470
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-10mdv2008.1
+ Revision: 133628
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-9mdv2007.0
+ Revision: 73306
- import perl-Audio-DSP-0.02-9mdv2007.0

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-9mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.02-8mdk
- Fix SPEC Using perl Policies
	- Source URL

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-7mdk
- spec cleanup
- rpmbuildupdate aware
- %%{1}mdv2007.1
- enable optimisations

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-6mdk
- rebuild for new perl

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.02-5mdk
- fix deps

