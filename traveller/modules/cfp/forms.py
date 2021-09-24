from modules.conf.models import Talk
from init import ModelForm


class SubmitTalkForm(ModelForm):
    class Meta:
        model = Talk
        exclude = ['accepted', 'slug', 'submitter_id', 'year']
        field_args = {
            'title': {
                'render_kw': {
                    'autocomplete': 'off',
                    'class': 'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150'
                }
            },
            'description': {
                'render_kw': {
                    'cols': 80,
                    'class': 'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150'
                }
            },
            'summary': {
                'render_kw': {
                    'cols': 80,
                    'class': 'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150'
                }
            },
            'notes': {
                'render_kw': {
                    'cols': 80,
                    'class': 'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150'
                }
            },
            'level': {
                'render_kw': {
                    'class': 'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150'
                }
            }
        }


class AdminTalkForm(ModelForm):
    class Meta:
        model = Talk
        exclude = ['submitter_id']
        field_args = {
            'title': {
                'render_kw': {
                    'autocomplete': 'off'
                }
            },
            'description': {
                'render_kw': {
                    'cols': 80
                }
            },
            'summary': {
                'render_kw': {
                    'cols': 80
                }
            },
            'notes': {
                'render_kw': {
                    'cols': 80
                }
            }
        }
