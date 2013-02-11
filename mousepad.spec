Summary:	Simple text editor for Xfce
Name:		mousepad
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/mousepad/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	dcfcdfaa8a19c89f35d5f6f64753e6e1
Patch0:		%{name}-desktop.patch
BuildRequires:	dbus-glib-devel
BuildRequires:	gtksourceview2-devel
BuildRequires:	pkg-config
Requires(post,postun): desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple text editor for Xfce.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/mousepad.desktop

