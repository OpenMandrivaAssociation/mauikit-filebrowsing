%define major 4

#define snapshot 20220106
%define libname %mklibname MauiKit-filebrowsing
%define oldlibname %mklibname MauiKit-filebrowsing 3
%define devname %mklibname -d MauiKit-filebrowsing

Name:		mauikit-filebrowsing
Version:	4.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	MauiKit File Browsing utilities and controls
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-filebrowsing/-/archive/%{?snapshot:master/mauikit-filebrowsing-master.tar.bz2#/mauikit-filebrowsing-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-filebrowsing-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
#BuildRequires:	cmake(KF5Plasma)
#BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)
#BuildRequires:	qt5-qtgraphicaleffects
#BuildRequires:	qt5-qtdeclarative
#BuildRequires:	qt5-qtquickcontrols2
Requires:	%{libname} = %{EVRD}

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{libname}
Summary:	Library files for mauikit-filebrowsing
Group:		System/Libraries
%rename %{oldlibname}
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for mauikit-filebrowsing

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{devname}
Summary:	Development files for mauikit-filebrowsing
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for mauikit-filebrowsing

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.


%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang mauikitfilebrowsing

%files -f mauikitfilebrowsing.lang
%{_libdir}/qt6/qml/org/mauikit/filebrowsing

%files -n %{libname}
%{_libdir}/libMauiKitFileBrowsing4.so.%{major}*

%files -n %{devname}
%{_includedir}/MauiKit4/FileBrowsing
%{_libdir}/cmake/MauiKitFileBrowsing4
%{_libdir}/libMauiKitFileBrowsing4.so
