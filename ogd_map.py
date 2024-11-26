import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from layer_data import layer_data
from streamlit_folium import st_folium
import folium


class Map():
    def __init__(self):
        self.layers = {}
        for k, v in layer_data.items():
            self.layers[k] = Layer(v)  
        data = {
            'id': [layer.id for layer in self.layers.values()],
            'layer': [layer for layer in self.layers.keys()],
            'label': [layer.label for layer in self.layers.values()],
        }
        self.layer_df = pd.DataFrame(data).set_index('layer')

    
    def layer_menu(self):
        with st.sidebar:
            event = st.dataframe(
                self.layer_df ,
                use_container_width=True,
                hide_index=True,
                on_select="rerun",
                selection_mode="multi-row",
            )
            for _, layer in self.layers.items():
                layer.de_select()
            for row in event.selection.rows:
                key = self.layer_df.index[row]
                self.layers[key].select()
        self.plot()

    def get_data(self):
        df = pd.DataFrame()
        return df
    
    def plot(self):
        df = pd.DataFrame()
        for _, layer in self.layers.items():
            if (layer.selected) and (len(layer.data))>0:
                df = pd.concat([df, layer.data])
        
        if len(df)>0:
            settings = {
                "width": 1000,
                "height": 800,
                "zoom": 14,
                "latitude": "latitude",
                "longitude": "longitude",
                "marker": "marker",
                "color": "color",
                "popup": "popup",
                "tooltip": "tooltip",
            }
            coordinates = [df[settings["latitude"]].mean(), df[settings["longitude"]].mean()]

            m = folium.Map(location=coordinates, zoom_start=settings["zoom"])
            for i in range(0, len(df)):
                folium.Marker(
                    id=i,
                    location=[df.iloc[i]['latitude'], df.iloc[i]['longitude']],
                    popup=df.iloc[i][settings['popup']],
                    icon=folium.Icon(color=df.iloc[i][settings['color']], icon=df.iloc[i][settings['marker']]),
                    tooltip=df.iloc[i][settings['tooltip']],
                ).add_to(m)
            st_data = st_folium(m, width = 1200, height = 1000)
            if st_data['last_object_clicked']:
                selected_df = df[(df['latitude'] == st_data['last_object_clicked']['lat']) & (df['longitude'] == st_data['last_object_clicked']['lng']) ]
                if len(selected_df)>0 and 'image_url' in selected_df.columns:
                    st.image(selected_df['image_url'].values[0])
            
        

class Layer():
    def __init__(self, item):
        self.id = item['id']
        self.label = item['label']
        self.geo_shape = item['geo_shape']
        self.color = item['color']
        self.icon = item['icon']
        self.fields = item['fields']
        self.popup_field = item['popup_field']
        self.base = item['base']
        self.image_url = item['image_url'] if 'image_url' in item else None
        self.pdf_url = item['pdf_url'] if 'pdf_url' in item else None
        self.field_names = [f[0] for f in self.fields] + [self.geo_shape]
        self.selected = False
        self.data = pd.DataFrame()
            
    def de_select(self):
        self.selected = False

    def select(self):
        self.selected = True
        if len(self.data)==0:
            with st.spinner(f"Loading {self.label} data..."):
                self.data = self.get_data()

    def get_data(self):
        def get_tooltip(row, fields):
            tooltip = ""
            for field in fields:
                tooltip += f'{field[1]}: {row[field[0]]}<br>'
            return tooltip
        
        try:
            url = self.get_data_url()
            df = pd.read_csv(url, delimiter=';')
            df = df[df[self.geo_shape].notna()]
            # Extract latitude and longitude
            df["latitude"] = df[self.geo_shape].apply(lambda x: float(x.split(",")[0]))
            df["longitude"] = df[self.geo_shape].apply(lambda x: float(x.split(",")[1]))
            # Generate tooltip for each row
            df["tooltip"] = df.apply(lambda row: get_tooltip(row, self.fields), axis=1)
            df['popup'] = df[self.popup_field]
            df['color'] = self.color
            df['marker'] = self.icon
            if self.image_url is not None:
                df = df.rename(columns={self.image_url: 'image_url'})
            if self.pdf_url is not None:
                df = df.rename(columns={self.pdf_url: 'pdf_url'})
            return df  
        except Exception as e:
            print(f"Error reading CSV: {e}")

    def init(self):
        pass 

    def __str__(self):
        return f'{self.id} {self.label}'

    def __repr__(self):
        return f'{self.id} {self.label}'
    
    def get_data_url(self):
        field_lst = self.field_names 
        if self.image_url is not None:
            field_lst += [self.image_url] 
        if self.pdf_url is not None:
            field_lst += [self.pdf_url] 
        fields_cli = ','.join(field_lst)
        return f'https://{self.base}/api/explore/v2.1/catalog/datasets/{self.id}/exports/csv?lang=de&timezone=Europe%2FBerlin&use_labels=false&delimiter=%3B&select={fields_cli}'
    

class School(Layer):
    def __init__(self, item):
        super().__init__(item)
    def __str__(self):
        return f'{self.name} {self.shape} {self.students}'

    def __repr__(self):
        return f'{self.name} {self.shape} {self.students}'