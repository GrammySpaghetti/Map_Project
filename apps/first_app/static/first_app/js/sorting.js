
L.Control.Sorch = L.Control.extend({
  onAdd: function(mymap){
    var div = L.DomUtil.create('div', 'bg-primary');
    div.style = 'width: 75px;';
    $(div).html('<div class="text-white"><p>This div Here</p></div>');
    return div;
  }

});
L.control.sorch = function(opts){
  return new L.Control.Sorch(opts);
}
