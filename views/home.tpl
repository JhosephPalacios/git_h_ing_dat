<html>

% include('_style_menu.tpl')
  <style>
    .blocked {
      pointer-events: none;
      animation: blink 13.4s infinite;
    }
    
    @keyframes blink {
      0% { opacity: 0; }
      50% { opacity: 0; }
      55% { opacity: 0.05; }
      57.5% { opacity: 0.1; }
      60% { opacity: 0.15; }
      75% { opacity: 0.7; }
      97% { opacity: 0.1; }
      100% { opacity: 0; }
    }
  </style>

<body>
  % include('_menu.tpl')



  % include('_footer.tpl')
</body>
</html>
