# seesaw (vendored)

Copied from https://github.com/ssieb/esphome_components/tree/23eb1124819261a3ea75585d8414f4ec65b50e2a/components/seesaw
and patched for ESPHome 2026.9, where `GPIOPin::dump_summary()` writes into a buffer instead of
returning a `std::string`. Drop this copy once upstream builds on 2026.9.

