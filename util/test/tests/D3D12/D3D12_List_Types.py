import renderdoc as rd
import rdtest


class D3D12_List_Types(rdtest.TestCase):
    demos_test_name = 'D3D12_List_Types'

    def check_capture(self):
        draw = self.find_draw("Draw")

        self.controller.SetFrameEvent(draw.eventId, False)

        self.check_triangle(out=draw.outputs[0], fore=[0.0, 1.0, 1.0, 1.0])

        postvs_data = self.get_postvs(draw, rd.MeshDataStage.VSOut, 0, draw.numIndices)

        postvs_ref = {
            0: {
                'vtx': 0,
                'idx': 0,
                'SV_POSITION': [-0.5, -0.5, 0.0, 1.0],
                'COLOR': [0.0, 1.0, 1.0, 1.0],
                'TEXCOORD': [1234.0, 5678.0],
            },
            1: {
                'vtx': 1,
                'idx': 1,
                'SV_POSITION': [0.0, 0.5, 0.0, 1.0],
                'COLOR': [0.0, 1.0, 1.0, 1.0],
                'TEXCOORD': [1234.0, 5678.0],
            },
            2: {
                'vtx': 2,
                'idx': 2,
                'SV_POSITION': [0.5, -0.5, 0.0, 1.0],
                'COLOR': [0.0, 1.0, 1.0, 1.0],
                'TEXCOORD': [1234.0, 5678.0],
            },
        }

        self.check_mesh_data(postvs_ref, postvs_data)

