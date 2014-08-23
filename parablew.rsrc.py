{'application':{'type':'Application',
          'name':'ParableW',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':u'Parable 2009',
          'size':(800, 587),
          'backgroundColor':(255, 255, 255),
          'icon':'svlogo_sm copy.ico',
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileOpenBank',
                   'label':u'Open &Bank\tAlt+B',
                   'command':'fileOpenBank',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileOpenSequence',
                   'label':u'&Open Sequence\tAlt+O',
                   'command':'fileOpen',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileImport',
                   'label':u'&Import Sequence\tAlt+I',
                   'command':'fileImport',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSave',
                   'label':u'&Save Sequence\tAlt+S',
                   'command':'fileSave',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextField', 
    'name':'KeyInput', 
    'position':(350, 500), 
    },

{'type':'StaticBox', 
    'name':'AutoPilotBox', 
    'position':(21, 139), 
    'size':(743, 342), 
    'label':'Auto Pilot', 
    'visible':False, 
    },

{'type':'ToggleButton', 
    'name':'btnAutoPilot', 
    'position':(590, 498), 
    'label':'Auto Pilot', 
    },

{'type':'Button', 
    'name':'btnKill', 
    'position':(679, 497), 
    'label':'ABORT!', 
    },

{'type':'CheckBox', 
    'name':'chkBeeps', 
    'position':(460, 504), 
    'label':'Beeps (testing only)', 
    },

{'type':'CheckBox', 
    'name':'chkUseBeat', 
    'position':(284, 505), 
    'label':'Use Beat', 
    },

{'type':'Button', 
    'name':'pbTap', 
    'position':(26, 495), 
    'size':(129, 30), 
    'label':'Tap to Set Beat', 
    },

{'type':'ImageButton', 
    'name':'ImageButton1', 
    'position':(212, 496), 
    'size':(39, 31), 
    'backgroundColor':(255, 255, 255, 255), 
    'border':'transparent', 
    'file':'svp.bmp', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(25, 488), 
    'size':(742, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(24, 134), 
    'size':(740, -1), 
    'layout':'horizontal', 
    },

{'type':'Slider', 
    'name':'slSeqRate', 
    'position':(262, 14), 
    'size':(236, -1), 
    'labels':False, 
    'layout':'horizontal', 
    'max':100, 
    'min':1, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':1, 
    },

{'type':'CheckBox', 
    'name':'chkLoop', 
    'position':(190, 13), 
    'label':'Loop', 
    },

{'type':'BitmapCanvas', 
    'name':'OutputCanvas1', 
    'position':(24, 44), 
    'size':(728, 75), 
    'backgroundColor':(255, 255, 255, 255), 
    },

{'type':'Button', 
    'name':'btnHello', 
    'position':(25, 5), 
    'size':(144, -1), 
    'label':'Run Sequence', 
    },

{'type':'Button', 
    'name':'align', 
    'position':(162, 496), 
    'size':(39, 30), 
    'label':'align', 
    },

] # end components
} # end background
] # end backgrounds
} }
