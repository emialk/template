include(FetchContent)

### Google test ###
# Used for unit tests
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        b796f7d44681514f58a683a3a71ff17c94edb0c1 # release-1.13.0
)

### Simple Directmedia Layer ###
# Used for 2D graphics and keyboard, mouse interaction	
FetchContent_Declare(
  sdl2
  GIT_REPOSITORY https://github.com/libsdl-org/SDL
  GIT_TAG        c4c034ca4bee77a8a7e73bd5cd553d47bd78be8f
)

FetchContent_MakeAvailable(googletest sdl2)
