Summary:	A GTK+ based DBF Editor
Summary(pl):	Oparty na GTK+ edytor DBF
Name:		gtkdbfeditor
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/gtkdbfeditor/%{name}-%{version}.tar.gz
# Source0-md5:	2e88b0e8d3c2cd0016ee7606782ef53d
URL:		http://gtkdbfeditor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK DBF Editor is a program to edit DBF files. It supports simple
editing functions.

%description -l pl
GTK DBF Editor to program do edycji plików DBF. Udostêpnia proste
mo¿liwo¶ci edycji.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gtkdbfeditor
%{_datadir}/%{name}
