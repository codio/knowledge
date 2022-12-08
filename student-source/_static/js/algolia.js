docsearch({
  // Your apiKey and indexName will be given to you once
  // we create your config
  apiKey: '7e59277e32050e11c2e8915f1b09d6e2',
  indexName: 'CodioDocs',
  appId: '0MJO9504F8', // Should be only included if you are running DocSearch on your own.
  // Replace inputSelector with a CSS selector
  // matching your search input
  container: '#docsearch',
  searchParameters: {
    hitsPerPage: 20,
  },  
  // Set debug to true to inspect the dropdown
  debug: false,
});
