/* -*- mode: js; coding: utf-8 -*- */

QARxisApp = angular.module(
    "QARxisApp", [],

    function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
    }
);
