'use strict';

var gulp = require('gulp');

var $ = require('gulp-load-plugins')();

gulp.task('settings:local', function () {
  return gulp.src('settings/local.json')
    .pipe($.ngConstant({
      name: 'settings'
    }))
    .pipe($.rename('settings.js'))
    .pipe(gulp.dest('app/scripts/'));
});
