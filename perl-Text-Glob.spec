Name: 		perl-Text-Glob
Version: 	0.08
Release: 	7%{?dist}
Summary: 	Perl module to match globbing patterns against text
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Text-Glob/
Source0: 	http://www.cpan.org/modules/by-module/Text/Text-Glob-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a filesystem.  If you
want to do full file globbing use the File::Glob module instead.

%prep
%setup -q -n Text-Glob-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-7
- add readme
- Related: rhbz#543948 

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.08-6.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.08-4
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.08-3
- rebuild for new perl

* Sat Aug 18 2007 Ralf Corsépius <rc040203@freenet.de> - 0.08-2
- Update license tag.

* Tue May 08 2007 Ralf Corsépius <rc040203@freenet.de> - 0.08-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.07-2
- Mass rebuild.

* Thu Jul 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0.07-1
- Upstream update.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 0.06-4
- Rebuild for perl-5.8.8.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 0.06-3
- Spec cleanup.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 0.06-2
- FE resubmission.

* Fri Jul 01 2005 Ralf Corsepius <ralf@links2linux.de> - 0.06-1
- FE submission.
