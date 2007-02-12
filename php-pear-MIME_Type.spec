%include	/usr/lib/rpm/macros.php
%define		_class		MIME
%define		_subclass	Type
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - utility class for dealing with MIME types
Summary(pl.UTF-8):   %{_pearname} - przydatna klasa do obsługi typów MIME
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dc2d377a121c6410d5f5c46e8ec32c03
URL:		http://pear.php.net/package/MIME_Type/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides functionality for dealing with MIME types.
- Parse MIME type.
- Supports full RFC2045 specification.
- Many utility functions for working with and determining info about
  types.
- Most functions can be called statically.
- Autodetect a file's MIME-type, either with mime_content_type() or
  the 'file' command.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa dostarcza funkcjonalności do obsługi typów MIME:
- przetwarzanie typu MIME,
- pełna obsługa specyfikacji RFC2045
- wiele przydatnych funkcji do obsługi i określania informacji na
  temat typów
- większość funkcji może być wywołana statycznie
- autodetekecja typu MIME pliku, za pomocą mime_content_type() lub z
  wykorzystaniem polecenia 'file'.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/docs .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/example.php
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
