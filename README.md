# Proyecto-Jaguarete-Kaa-SA
Página web 🛒🏃‍♀️ e-commer, fue realizado con el fin del Trabajo Final del curso PoloTic. Diseño adaptable.


![1](https://user-images.githubusercontent.com/91395402/221860544-61939870-5b48-4bd2-96e0-26b57608b4bb.jpg)

.container-fluid {
  height: 90%;
  width: 100%;
}

.carousel-inner img {
  height: 300px;
}

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>

<div class="container-fluid bg-primary">
  <div class="row bg-dark">

    <!-- ================== 1-carousel bootstrap  ==================  -->
    <div id="carousel1_indicator" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carousel1_indicator" data-slide-to="0" class="active"></li>
        <li data-target="#carousel1_indicator" data-slide-to="1"></li>
        <li data-target="#carousel1_indicator" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" src="https://picsum.photos/750/400/?random" alt="First slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="https://picsum.photos/750/400/?random" alt="Second slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="https://picsum.photos/750/400/?random" alt="Third slide">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carousel1_indicator" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carousel1_indicator" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
