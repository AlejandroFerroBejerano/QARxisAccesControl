/* -*- mode: js; coding: utf-8 -*- */
var app= new Vue({
   el: '#pending_events',
   delimiters: ['[[',']]'],
   data: {
   events: [],
   event_status: null,
   sortKey: 'name',
   search: '',
   loading: false,
   currentEvent: {},
   message: null,
   newEvent: { 'event_date': null, 'event_time': null, 'event_kind': null, 'event_des': null, 'event_location': null, 'event_status': null },
   timer: 300000
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
 getStatus: function(id) {
   this.loading = true;
   this.$http.get('/api/state/' + id)
       .then((response) => {
         this.event_status = response.data;
         this.loading = false;
       })
       .catch((err) => {
         this.loading = false;
         console.log(err);
       })
 },
 sortBy: function(sortKey){
   this.reverse = (this.sortKey == sortKey) ? ! this.reverse: false;
   this.sortKey = sortKey;
 }
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
 },
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
computed: {
    date(){
    return event.get_date ()
    },
  }
});
