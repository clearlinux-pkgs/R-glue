#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-glue
Version  : 1.3.1
Release  : 21
URL      : https://cran.r-project.org/src/contrib/glue_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/glue_1.3.1.tar.gz
Summary  : An implementation of interpreted string literals for R.
Group    : Development/Tools
License  : MIT
Requires: R-glue-lib = %{version}-%{release}
BuildRequires : R-DBI
BuildRequires : R-RSQLite
BuildRequires : R-evaluate
BuildRequires : buildreq-R

%description
# glue <a href='https:/glue.tidyverse.org'><img src='man/figures/logo.png' align="right" height="139" /></a>

%package lib
Summary: lib components for the R-glue package.
Group: Libraries

%description lib
lib components for the R-glue package.


%prep
%setup -q -c -n glue

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552438430

%install
export SOURCE_DATE_EPOCH=1552438430
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glue
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glue
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glue
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library glue|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/glue/DESCRIPTION
/usr/lib64/R/library/glue/INDEX
/usr/lib64/R/library/glue/LICENSE
/usr/lib64/R/library/glue/Meta/Rd.rds
/usr/lib64/R/library/glue/Meta/features.rds
/usr/lib64/R/library/glue/Meta/hsearch.rds
/usr/lib64/R/library/glue/Meta/links.rds
/usr/lib64/R/library/glue/Meta/nsInfo.rds
/usr/lib64/R/library/glue/Meta/package.rds
/usr/lib64/R/library/glue/Meta/vignette.rds
/usr/lib64/R/library/glue/NAMESPACE
/usr/lib64/R/library/glue/NEWS.md
/usr/lib64/R/library/glue/R/glue
/usr/lib64/R/library/glue/R/glue.rdb
/usr/lib64/R/library/glue/R/glue.rdx
/usr/lib64/R/library/glue/doc/index.html
/usr/lib64/R/library/glue/doc/speed.R
/usr/lib64/R/library/glue/doc/speed.Rmd
/usr/lib64/R/library/glue/doc/speed.html
/usr/lib64/R/library/glue/doc/transformers.R
/usr/lib64/R/library/glue/doc/transformers.Rmd
/usr/lib64/R/library/glue/doc/transformers.html
/usr/lib64/R/library/glue/help/AnIndex
/usr/lib64/R/library/glue/help/aliases.rds
/usr/lib64/R/library/glue/help/figures/logo.png
/usr/lib64/R/library/glue/help/glue.rdb
/usr/lib64/R/library/glue/help/glue.rdx
/usr/lib64/R/library/glue/help/paths.rds
/usr/lib64/R/library/glue/html/00Index.html
/usr/lib64/R/library/glue/html/R.css
/usr/lib64/R/library/glue/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/glue/libs/glue.so
/usr/lib64/R/library/glue/libs/glue.so.avx2
/usr/lib64/R/library/glue/libs/glue.so.avx512
