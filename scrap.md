# Scrap code

## Publications.md
<body>
<link rel="stylesheet" media="screen" href="css/style.css">
<!-- particles.js container -->
<div id="particles-js"></div>

<!-- scripts -->
<script src="js/particles.js"></script>
<script src="js/app.js"></script>

</body>


## base.html
<link rel="stylesheet" media="screen" href="style.css">
<!-- particles.js container -->
<div id="particles-js"></div>

<!-- scripts -->
<script src="particles.js"></script>
<script src="app.js"></script>



<link rel="stylesheet" href="{{ SITEURL }}/theme/css/particle-js-style.css" type="text/css" media="all">
<!-- particles.js container -->
<div id="particles-js"><canvas class="particles-js-canvas-el" width="1163" height="2458" style="width: 100%; height: 100%;"></canvas></div>

<!-- scripts -->
<script type="text/javascript" src="{{ SITEURL }}/theme/js/particles.min.js"></script>
<script type="text/javascript" src="{{ SITEURL }}/theme/js/particles-config.js"></script>

Line 50 in base.html

<div class="tagline">
    {% if TAGS_URL %}
      {% for tag, articles in tags|sort %}
        <a href="{{ SITEURL }}/{{ tag.url }}" {{ 'class="active"' if  output_file == tag.url }}>{{ tag }} ({{ articles|count }})</a> &#124;
      {% endfor %}
    {% endif %}
    {% if ARCHIVES_URL %}
        <a href="{{ SITEURL }}/{{ ARCHIVES_URL }}" {{ 'class="active"' if  output_file == ARCHIVES_URL }}>{{ 'Archives ('+ articles|count|string + ')' if  articles|count > all_articles|count  else 'Archives (' + all_articles|count|string + ')'}}</a>
    {% endif %}
</div>



<canvas class="particles-js-canvas-el" width="1178" height="415" style="width: 100%; height: 100%;"></canvas>


<div id="particles-js"><canvas class="particles-js-canvas-el" width="1163" height="2458" style="width: 100%; height: 100%;"></canvas></div>


<script src="/js/particles.min.js"></script>
<script src="/js/particles-config.js"></script>



<link rel="stylesheet" href="{{ SITEURL }}/theme/css/particle-js-style.css" type="text/css" media="all">
<!-- particles.js container -->
<div id="particles-js"><canvas class="particles-js-canvas-el" width="1163" height="2458" style="width: 100%; height: 100%;"></canvas></div>

<!-- scripts -->
<script type="text/javascript" src="{{ SITEURL }}/theme/js/particles.min.js"></script>
<script type="text/javascript" src="{{ SITEURL }}/theme/js/particles-config.js"></script>
<script type="text/javascript" src="{{ SITEURL }}/theme/js/particles.js"></script>




In index.html


<!-- Typed.js -->
<script src="/js/jquery-1.11.2.min.js"></script>
<script src="/js/typed.js" type="text/javascript"></script>
<script>
  $(function(){
    $(".typed").typed({
      strings: ["mathematician.", "journalist.", "data scientist.", "media producer."],
      typeSpeed: 85,
      loop: true,
      backDelay: 1000
    });
  });
</script>

<div class="typed-js-hide">
  <div class="row">
    <div class="col-sm-12">
      <div class="text-center">
          <h1>I am a <span class="typed" style="color:#f70097";></span></h1>
      </div>
    </div>
  </div>
</div>



Through these research projects I have developed sound mathematical and computational skills. During my studies and further academic work I’ve been able to demonstrate a capacity to work independently and to collaborate with people at varying levels. I have also demonstrated an ability to communicate eﬀectively with external collaborators.
