// <![CDATA[
            mapboxgl.accessToken = 'pk.eyJ1IjoiYWNrYWhibGF5eSIsImEiOiJjajcyOXM3a28wZzMxMndtbnk5d2gya290In0.uV6dgDoaM-3Um-xWKyLegQ';
            var map = new mapboxgl.Map({
                container: 'map',
                style: 'mapbox://styles/ackahblayy/cjaeffm5d643z2snwjtagcu0n',
                center: [0.019, 8.034],
                zoom: 5.6,
                minZoom:5,
                maxZoom:15,
                attributionControl: false
            });
            
            // add attribute 
            map.addControl(new mapboxgl.AttributionControl(), 'top-right');
            //Display Navigation controls 
            var nav = new mapboxgl.NavigationControl();
            map.addControl(nav, 'bottom-right');
            // Add geolocate control to the map.
            var geo = new mapboxgl.GeolocateControl({
                positionOptions: {
                    enableHighAccuracy: true
                },
                trackUserLocation: true
            });
            map.addControl(geo, 'bottom-right');
            
            
            
            
            map.on('click', function(e) {
              var features = map.queryRenderedFeatures(e.point, {
                layers: ['gs-plaza', 'accra-city-hotel', 'the-octagon', 'silver-star-tower', 'mvenpick-ambassador-hotel', 'marina-mall', 'royal-senkyi'] // replace this with the name of the layer
              });
              
              if (!features.length) {
                return;
              }
            
              var feature = features[0];
            
            
             // map.easeTo({center: feature.geometry.coordinates});
            
              var popup = new mapboxgl.Popup({ offset: [0, -15], closeButton: false, closeOnClick: false })
                .setLngLat(feature.geometry.coordinates)
                .setHTML('<div>'+
                '<img class="img-fluid" src="'+ feature.properties.image +'" alt="Card image cap">'
            +
                //Card content
                '<div class="card-body">'
                +
                    //Title
                    '<h4 class="card-title">'+ feature.properties.title +'</h4>'
                    +
                    //Text
                    '<p class="card-text">'+ feature.properties.description +'</p>'
                    +
                    '<a href="'+ feature.properties.link +'" class="btn btn-primary">Take a virtual Tour</a>'
                    +
                '</div>'
                +
            
            '</div>'             
                )
                .setLngLat(feature.geometry.coordinates)
                .addTo(map);
            });
            // Zoom in on the regions 
            map.on('click', function(e){
              var regionFeatures = map.queryRenderedFeatures(e.point,{
                  layers: ['regions-in-ghana']
              });
            
              if(!regionFeatures.length){
                  return;
              }
              var regionfeature = regionFeatures[0];
            
              map.easeTo({
                center: regionfeature.geometry.coordinates,
                zoom: 10.5
            
              });
            });
            //City zoom 
            map.on('click', function(e){
              var Features = map.queryRenderedFeatures(e.point,{
                  layers: ['place-city-lg-n','place-city-lg-s','place-city-md-n','place-city-md-s']
              });
            
              if(!Features.length){
                  return;
              }
              var feature = Features[0];
            
              map.easeTo({
                center: feature.geometry.coordinates,
                zoom: 11.5
            
              });
            });
            // Town Zoom
            map.on('click', function(e){
              var Features = map.queryRenderedFeatures(e.point,{
                  layers: ['place-town','place-city-sm']
              });
            
              if(!Features.length){
                  return;
              }
              var feature = Features[0];
            
              map.easeTo({
                center: feature.geometry.coordinates,
                zoom: 13.1
            
              });
            });
            // ]]>