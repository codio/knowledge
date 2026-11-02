(function () {
  // Identical output for every build: the audience comes from the page's own meta tag.
  var meta = document.querySelector('meta[name="docsearch:audience"]');
  var audience = meta ? meta.getAttribute("content") : "";
  var params = {};
  if (audience) {
    params.facetFilters = (params.facetFilters || []).concat(["audience:" + audience]);
  }
  docsearch({
    container: "#docsearch",
    appId: "0MJO9504F8",
    apiKey: "7e59277e32050e11c2e8915f1b09d6e2",
    indexName: "CodioDocs",
    searchParameters: params
  });
})();