#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-km.ci
Version  : 0.5.6
Release  : 1
URL      : https://cran.r-project.org/src/contrib/km.ci_0.5-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/km.ci_0.5-6.tar.gz
Summary  : Confidence Intervals for the Kaplan-Meier Estimator
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n km.ci

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713891881

%install
export SOURCE_DATE_EPOCH=1713891881
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/km.ci/DESCRIPTION
/usr/lib64/R/library/km.ci/INDEX
/usr/lib64/R/library/km.ci/Meta/Rd.rds
/usr/lib64/R/library/km.ci/Meta/data.rds
/usr/lib64/R/library/km.ci/Meta/features.rds
/usr/lib64/R/library/km.ci/Meta/hsearch.rds
/usr/lib64/R/library/km.ci/Meta/links.rds
/usr/lib64/R/library/km.ci/Meta/nsInfo.rds
/usr/lib64/R/library/km.ci/Meta/package.rds
/usr/lib64/R/library/km.ci/NAMESPACE
/usr/lib64/R/library/km.ci/NEWS
/usr/lib64/R/library/km.ci/R/km.ci
/usr/lib64/R/library/km.ci/R/km.ci.rdb
/usr/lib64/R/library/km.ci/R/km.ci.rdx
/usr/lib64/R/library/km.ci/data/rectum.dat.rda
/usr/lib64/R/library/km.ci/help/AnIndex
/usr/lib64/R/library/km.ci/help/aliases.rds
/usr/lib64/R/library/km.ci/help/km.ci.rdb
/usr/lib64/R/library/km.ci/help/km.ci.rdx
/usr/lib64/R/library/km.ci/help/paths.rds
/usr/lib64/R/library/km.ci/html/00Index.html
/usr/lib64/R/library/km.ci/html/R.css