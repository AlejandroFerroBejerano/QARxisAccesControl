/* -*- mode: js; coding: utf-8 -*- */
const app = new Vue({
   el: '#pending_events',
   delimiters: ['[[',']]'],
   data: {
     events: [],
     event_status: null,
     currentSort: 'time',
     currentSortDir: 'asc',
     search: '',
     currentEvent: {},
     message: null,
     sort_events: [],
     timer: 5000
   },
   mounted: function() {
     this.getEvents();
     setInterval(function() {
       this.getEvents();
     }.bind(this), this.timer);
   },
   created:function() {
     this.getEvents();
   },
   methods: {
     getEvents:function() {
       this.$http.get('/api/').then((response) => {
            this.events = response.data;
          }).bind(this);
      },
      getEvent:function(id) {
        this.$http.get('/api/' + id)
          .then((response) => {
            this.currentEvent = response.data;
          })
          .catch((err) => {
            console.log(err);
          })
      },
      getStatus:function(id) {
        this.$http.get('/api/state/' + id)
          .then((response) => {
            this.event_status = response.data;
          })
        .catch((err) => {
          console.log(err);
        })
      },
      getDate:function(timestamp){
        return timestamp.split('T')[0]
      },
      getTime:function(timestamp){
        return timestamp.split('T')[1].split('+')[0]
      },
      sort:function(sortKey){
        if(sortKey === this.currentSort){
          this.currentSortDir = this.currentSortDir === 'asc'?'desc':'asc';
        }
        this.currentSort = sortKey;
      },
   },
  computed: {
    sortedEvents:function(){
      this.sort_events = this.events.sort((a,b) => {
        let modifier = 1;
        if (this.currentSortDir === 'desc') modifier = -1;
        if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
        if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        return 0;
      });
      return this.sort_events;
    },
    filteredEvents() {
      return this.sortedEvents.filter(event => {
        return event.timestamp.toLowerCase().includes(this.search.toLowerCase())
      });
    },
  }
});
