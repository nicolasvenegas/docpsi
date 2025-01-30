
  <!-- FOOTER -->
  <footer class="social-footer">
    <div class="social-footer-left">
      <a href="https://www.ufro.cl" target="_blank"><img class="logo" src="assets/Logo-2022-UFRO.png"></a>
    </div>
    <div class="social-footer-icons">
      <ul class="menu simple">
        <li><a href="https://www.facebook.com/">facebook</a></li>
        <li><a href="https://www.instagram.com/?hl=en">Instagram</a></li>
      </ul>
    </div>
  </footer>
  
  




  <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/what-input/5.2.12/what-input.min.js" integrity="sha512-jdMp80Gf2e7K/JH3+mucRwyeRaqRPD+ykSpkmbBqxWMMCfEZEL9PF0zzF3JEgV4IVNj6eTjV8X41e7Gz5nNwyA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/6.9.0/js/foundation.min.js" integrity="sha512-P4f0g0iAkyfUF2V2VX8dxkoBxPLULaV2TM8HQGXFRb75AzLVAf+sn+MRweu/C81rL2JaYutbY6cWAbmwJbtOcg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
  <script src="js/app.js"></script>
  <!--Smooth scroll-->
  <script>
    const lenis = new Lenis()
    lenis.on('scroll', (e) => {
      console.log(e)
    })
    function raf(time) {
      lenis.raf(time)
      requestAnimationFrame(raf)
    }
    requestAnimationFrame(raf)
  </script>
</body>

</html>