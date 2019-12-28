from django import forms


class GetAuctions(forms.Form):
    region = forms.ChoiceField(choices=[('eu', 'EU')])
    # list of english servers in europe
    server = forms.ChoiceField(choices=[('Draenor', 'Draenor'), ('Kazzak', 'Kazzak'),
                                        ('Ragnaros', 'Ragnaros'), ('Ravencrest', 'Ravencrest'),
                                        ('Twisting Nether', 'Twisting Nether'), ('Tarren mill', 'Tarren Mill'),
                                        ('Burning Legion', 'Burning Legion'), ('Silvermoon', 'Silvermoon'),
                                        ('Stormreaver', 'Stormreaver'), ("Drak'thul", "Drak'thul"),
                                        ('Stormscale', 'Stormscale'), ('Argent Dawn', 'Argent Dawn'),
                                        ('Sylvanas', 'Sylvanas'), ('Defias Brotherhood', 'Defias Brotherhood'),
                                        ('Magtheridon', 'Magtheridon'), ('Outland', 'Outland'),
                                        ('Sunstrider', 'Sunstrider'), ('Grim Batol', 'Grim Batol'),
                                        ('Doomhammer', 'Doomhammer'), ('The Maelstrom', 'The Maelstrom'),
                                        ('Shattered Hand', 'Shattered Hand'), ('Arathor', 'Arathor'),
                                        ('Frostmane', 'Frostmane'), ('Emerald Dream', 'Emerald Dream'),
                                        ('Azjol-Nerub', 'Azjol-Nerub'), ('Kilrogg', 'Kilrogg'),
                                        ('Thunderhorn', 'Thunderhorn'), ("Twilight's Hammer", "Twilight's Hammer"),
                                        ('Aggramar', 'Aggramar'), ('Shadowsong', 'Shadowsong'),
                                        ('Nordrassil', 'Nordrassil'), ('Chamber of Aspects', 'Chamber of Aspects'),
                                        ('Alonsus', 'Alonsus'), ('Darksorrow', 'Darksorrow'),
                                        ('Stormrage', 'Stormrage'), ('Bloodhoof', 'Bloodhoof'),
                                        ('Frostwhisper', 'Frostwhisper'), ('Darkspear', 'Darkspear'),
                                        ('Auchindoun', 'Auchindoun'), ('Dragonblight', 'Dragonblight'),
                                        ('Eonar', 'Eonar'), ('Moonglade', 'Moonglade'),
                                        ("Al'Akir", "Al'Akir"), ('Aerie Peak', 'Aerie Peak'),
                                        ('Lightbringer', 'Lightbringer'), ('Earthen Ring', 'Earthen Ring')])
    # restricting the amount of auctions to see at the same time to prevent crashes, pagination is a future solution
    amount = forms.IntegerField(min_value=1, max_value=30)
