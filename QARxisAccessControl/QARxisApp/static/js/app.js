/* -*- mode: js; coding: utf-8 -*- */
new Vue({
   el: '#pending_events',
   delimiters: ['[[',']]'],
   data: {
   events: [],
   loading: false,
   currentEvent: {},
   message: null,
   newArticle: { 'article_heading': null, 'article_body': null },
   timer: 3000
 },
 mounted: function() {
   this.getEvents();
   setInterval(function() {
     this.getEvents();
   }.bind(this), this.timer);
 },
 methods: {
  getEvents: function() {
  this.loading = true;
  this.$http.get('/api/').then((response) => {
        this.events = response.data;
        this.loading = false;
      }).bind(this);
 },
 getEvent: function(id) {
  this.loading = true;
  this.$http.get('/api/' + id)
      .then((response) => {
        this.currentEvent = response.data;
        this.loading = false;
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 },
 /*addArticle: function() {
  this.loading = true;
  this.$http.post('/api/article/',this.newArticle)
      .then((response) => {
        this.loading = false;
        this.getArticles();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 },*/
 updateEvent: function() {
  this.loading = true;
  console.log(this.currentEvent);
  this.$http.put('/api/article/' + this.currentEvent.event_id + '/', this.currentEvent)
      .then((response) => {
        this.loading = false;
        this.currentEvent = response.data;
        this.getArticles();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 },
 /*deleteArticle: function(id) {
  this.loading = true;
  this.$http.delete('/api/article/' + id )
      .then((response) => {
        this.loading = false;
        this.getArticles();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 }*/
 },
});
