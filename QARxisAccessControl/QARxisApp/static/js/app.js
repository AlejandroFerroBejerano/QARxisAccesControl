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
      }).bind(this, this.timer);
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
 getDate: function(timestamp){
   return timestamp.split('T')[0]
 },
 getTime: function(timestamp){
   return timestamp.split('T')[1].split('+')[0]
 },
 sortBy: function(sortKey){
   this.reverse = (this.sortKey == sortKey) ? ! this.reverse: false;
   this.sortKey = sortKey;
 }
},
computed: {
  }
});
