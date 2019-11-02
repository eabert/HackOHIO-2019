if (!window.dash_clientside) {
    window.dash_clientside = {}
}

window.dash_clientside.clientside = {

   figure: function (fig_dict, zoom) {

       if (!fig_dict) {
           throw "Figure data not loaded, aborting update."
       }

       // Copy the fig_data so we can modify it
       fig_dict_copy = {...fig_dict};

       fig_dict_copy["layout"]["mapbox"]["zoom"] = zoom;

       return fig_dict_copy

   },

}