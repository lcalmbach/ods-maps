# colors = ['black', 'beige', 'lightblue', 'gray', 'blue', 'darkred', 'lightgreen', 'purple', 'red', 'green', 'lightred', 'white', 'darkblue', 'darkpurple', 'cadetblue', 'orange', 'pink', 'lightgray', 'darkgreen']


layer_data = {
    'schulstandort': {
        'base': 'data.bs.ch',
        'id': '100029',
        'label': 'Schulstandorte Gemeinde Basel',
        'geo_shape': 'geo_point_2d',
        'fields': [('sc_schulstandort','Bezeichnung'), ('sc_schultyp', 'Art'), ('sc_adresse', 'Adresse')],
        'popup_field': 'sc_schulstandort',
        'color': 'blue',
        'icon': 'home',
    },
    'schulstandort-riehen-bettingen': {
        'base': 'data.bs.ch',
        'id': '100030',
        'label': 'Schulstandorte Gemeinden Riehen/Bettingen',
        'geo_shape': 'geo_point_2d',
        'fields': [('standort','Bezeichnung'), ('typ', 'Typ'),  ('ort', 'Ort')],
        'popup_field': 'standort',
        'color': 'lightred',
        'icon': 'home',
    },

    'haltestellen': {
        'base': 'data.bs.ch',
        'id': '100063',
        'label': 'Haltestellen des öffentlichen Verkehrs',
        'geo_shape': 'geo_point_2d',
        'fields':  [('name','Haltestellenname'), ('tu_nr', 'Transportunternehmen_Name'), ('gde', 'Gemeinde'), ('kt', 'Gebiet')],
        'popup_field': 'name',
        'color': 'red',
        'icon': 'home',
    },

    'kunst_oeff_raum': {
        'base': 'data.bs.ch',
        'id': '100214',
        'label': 'Kunst im öffentlichen Raum',
        'geo_shape': 'geo_point_2d',
        'fields':  [('gruppe','Gruppe'), ('ku_name', 'Kunstschaffende'), ('datierung', 'Datierung')],
        'popup_field': 'gruppe',
        'color': 'green',
        'icon': 'arrow-up',
        'image_url': 'foto_downloadlink',
        'doc_url': 'pdf',
    },
    'smart_climate_stationen': {
        'base': 'data.bs.ch',
        'id': '100082',
        'label': 'Standorte Mess-Stationen Smart Climate Luftklima',
        'geo_shape': 'coords',
        'fields':  [('name_original','Station-ID'), ('dates_min_date', 'Werte seit'), ('dates_max_date', 'Werte bis'), ('stadtklima_basel_link', 'link')],
        'popup_field': 'name_original',
        'color': 'gray',
        'icon': 'arrow-up',
        'doc_url': 'stadtklima_basel_link',
    },
    'bohrkataster': {
        'base': 'data.bs.ch',
        'id': '100182',
        'label': 'Bohrkataster',
        'geo_shape': 'geo_point_2d',
        'fields':  [('art','Art der Bohrung'), ('id_bohrung', 'Identifikator'), ('rohrdurchm', 'Durchmesser mm'), ('erstellung', 'Bohrjahr'), ('strasse', 'Strasse'), ('hausnummer', 'Hausnummer')],
        'popup_field': 'id_bohrung',
        'color': 'gray',
        'icon': 'arrow-down',
    },
    'ladestationen': {
        'base': 'data.bs.ch',
        'id': '100005',
        'label': 'IWB Ladestationen für Elektroautos',
        'geo_shape': 'geo_point_2d',
        'fields':  [('name','Name'), ('beschreibung', 'Beschreibung'), ('art', 'Art'), ('ort', 'Ort')],
        'popup_field': 'name',
        'color': 'lightblue',
        'icon': 'bookmark',
    }
}
