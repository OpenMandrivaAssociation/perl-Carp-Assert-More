%define module	Carp-Assert-More
%define name	perl-%{module}
%define version	1.12
%define release	%mkrel 2

Name:		%{name}
Version: 	%{version}
Release:	%{release}
Summary:	Convenience wrappers around Carp::Assert module
License: 	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl-Carp-Assert
BuildRequires:  perl-Test-Exception
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Carp::Assert::More is a set of wrappers around the Carp::Assert functions 
to make the habit of writing assertions even easier.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Carp
%{_mandir}/man3/*


