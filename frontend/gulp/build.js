'use strict';

var gulp = require('gulp');
var yargs = require('yargs');

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license']
});

gulp.task('styles', function () {
  if (yargs.argv.buildScss) {
    return gulp.src('app/styles/main.scss')
      .pipe($.plumber())
      .pipe($.rubySass({style: 'expanded'}))
      .pipe($.autoprefixer('last 1 version'))
      .pipe(gulp.dest('app/styles'))
      .pipe($.size());
  }
});

gulp.task('scripts', function () {
  return gulp.src(['app/scripts/**/*.js', '!app/scripts/settings.js'])
    .pipe($.jshint())
    .pipe($.jshint.reporter('jshint-stylish'))
    .pipe($.size());
});

gulp.task('partials', function () {
  return gulp.src('app/partials/**/*.html')
    .pipe($.minifyHtml({
      empty: true,
      spare: true,
      quotes: true
    }))
    .pipe($.ngHtml2js({
      moduleName: 'lightningtalks',
      prefix: 'partials/'
    }))
    .pipe(gulp.dest('.tmp/partials'))
    .pipe($.size());
});

gulp.task('html', ['styles', 'scripts', 'partials'], function () {
  var jsFilter = $.filter('**/*.js');
  var cssFilter = $.filter('**/*.css');

  return gulp.src('app/*.html')
    .pipe($.inject(gulp.src('.tmp/partials/**/*.js'), {
      read: false,
      starttag: '<!-- inject:partials -->',
      addRootSlash: false,
      addPrefix: '../'
    }))
    .pipe($.useref.assets())
    .pipe($.rev())
    .pipe(jsFilter)
    .pipe($.ngAnnotate())
    .pipe($.uglify({preserveComments: $.uglifySaveLicense}))
    .pipe(jsFilter.restore())
    .pipe(cssFilter)
    .pipe($.replace('bower_components/bootstrap-sass-official/vendor/assets/fonts/bootstrap','fonts'))
    .pipe($.csso())
    .pipe(cssFilter.restore())
    .pipe($.useref.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe(gulp.dest('dist'))
    .pipe($.size());
});

gulp.task('images', function () {
  return gulp.src('app/images/**/*')
    .pipe($.cache($.imagemin({
      optimizationLevel: 3,
      progressive: true,
      interlaced: true
    })))
    .pipe(gulp.dest('dist/images'))
    .pipe($.size());
});

gulp.task('fonts', function () {
  return gulp.src($.mainBowerFiles())
    .pipe($.filter('**/*.{eot,svg,ttf,woff}'))
    .pipe($.flatten())
    .pipe(gulp.dest('dist/fonts'))
    .pipe($.size());
});

gulp.task('clean', function () {
  return gulp.src(['.tmp', 'dist'], { read: false }).pipe($.rimraf());
});

gulp.task('build', ['settings:local', 'html', 'partials', 'images', 'fonts']);
