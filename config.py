# 3DMark
ul_3dmarks = [
    "steelnomad_dx12.3dmdef",
    "speedway.3dmdef",
    "solarbay.3dmdef",
    "portroyal.3dmdef"
    "timespy.3dmdef",
    "timespy_extreme.3dmdef"
]

ul_procyons = {
    "cuda": [
        "configs/ai_computer_vision_tensorrt_f16.def",
        "configs/ai_computer_vision_tensorrt_f32.def",
        "configs/ai_imagegeneration_sd15fp16_tensorrt.def",
        "configs/ai_imagegeneration_sdxlfp16_tensorrt.def",
    ],
    "xpu": [
        "configs/ai_computer_vision_openvino_f16.def",
        "configs/ai_computer_vision_openvino_f32.def",
        "configs/ai_imagegeneration_sd15fp16_openvino.def",
        "configs/ai_imagegeneration_sdxlfp16_openvino.def",
    ]
}